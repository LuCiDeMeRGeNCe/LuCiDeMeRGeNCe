#!/usr/bin/env python3
"""Check internal repository links and the optional published Pages smoke test."""
import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
REPO = "https://github.com/LuCiDeMeRGeNCe/LuCiDeMeRGeNCe"
SITE = "https://lucidemergence.github.io/LuCiDeMeRGeNCe/"
OLD = "https://github.com/" + "secrecy99-art/LuCiDeMeRGeNCe"
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]+\")?\)")

class HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "id" in values:
            self.ids.add(values["id"])
        for key in ("href", "src"):
            if values.get(key):
                self.urls.append(values[key])

def validate():
    errors = []
    checked = 0
    for file in sorted(ROOT.rglob("*")):
        if not file.is_file() or ".git" in file.parts or "__pycache__" in file.parts:
            continue
        if file.suffix not in (".md", ".html", ".txt", ".json", ".xml", ".yml", ".yaml"):
            continue
        rel = file.relative_to(ROOT)
        body = file.read_text(encoding="utf-8")
        if OLD in body:
            errors.append(str(rel) + ": obsolete repository URL")
        links = []
        ids = set()
        if file.suffix == ".md" or file.name == "llms.txt":
            links.extend(m.group(1) for m in MARKDOWN_LINK.finditer(body))
        if file.suffix == ".html":
            parser = HTMLLinks()
            parser.feed(body)
            links += parser.urls
            ids = parser.ids
        if file.suffix == ".json":
            try:
                data = json.loads(body)
                if file.name == "PROJECT.json":
                    for key in ("workstreams", "fiction_archive", "discovery_files"):
                        links += data.get(key, [])
                    if data.get("repository") != REPO or data.get("website") != SITE:
                        errors.append(str(rel) + ": incorrect canonical project metadata")
            except json.JSONDecodeError as exc:
                errors.append(str(rel) + ": invalid JSON: " + str(exc))
        if file.suffix == ".xml":
            try:
                ElementTree.fromstring(body)
            except ElementTree.ParseError as exc:
                errors.append(str(rel) + ": invalid XML: " + str(exc))
        for link in links:
            checked += 1
            link = link.strip("<>")
            if not link or link.startswith(("mailto:", "tel:", "data:")):
                continue
            if link.startswith("#"):
                if file.suffix == ".html" and link[1:] not in ids:
                    errors.append(str(rel) + ": nonexistent page anchor " + link)
                continue
            if link.startswith(REPO + "/blob/main/"):
                target = ROOT / unquote(urlsplit(link).path.split("/blob/main/", 1)[1])
            elif link.startswith(REPO + "/tree/main/"):
                target = ROOT / unquote(urlsplit(link).path.split("/tree/main/", 1)[1])
            elif link.startswith(SITE):
                target = ROOT / "docs" / (unquote(link[len(SITE):].split("#", 1)[0].split("?", 1)[0]) or "index.html")
            elif link.startswith(("https://", "http://")):
                continue
            else:
                relative = unquote(link.split("#", 1)[0].split("?", 1)[0])
                target = file.parent / relative
            resolved = target.resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(str(rel) + ": missing target " + link)
    return checked, errors

def check_live():
    errors = []
    for suffix in ("", "llms.txt", "robots.txt", "sitemap.xml"):
        url = SITE + suffix
        try:
            with urlopen(Request(url, headers={"User-Agent": "LuCiDeMeRGeNCe-link-health/1.0"}), timeout=20) as response:
                content = response.read()
                if response.status != 200 or not content:
                    errors.append(url + ": unexpected HTTP status or empty document")
                if not suffix and b"LuCiDeMeRGeNCe" not in content:
                    errors.append(url + ": project marker absent from homepage")
        except Exception as exc:
            errors.append(url + ": " + str(exc))
    return errors

def main():
    args = argparse.ArgumentParser()
    args.add_argument("--live", action="store_true", help="Also check the published GitHub Pages endpoints")
    opt = args.parse_args()
    checked, errors = validate()
    if opt.live:
        errors += check_live()
    for error in errors:
        print("FAIL:", error)
    if errors:
        print("Link integrity failed:", len(errors), "problem(s)")
        return 1
    print("PASS:", checked, "references checked; local paths and canonical ownership validated" + ("; public Pages endpoints responded" if opt.live else ""))
    return 0

if __name__ == "__main__":
    sys.exit(main())
