# Canonical records and optional social editions

## One source of truth

Maintain structured, versioned records in `discourse/records/` and machine-readable indexes in `discourse/topics.yaml`. The GitHub repository is the canonical data store for this pilot, not a live database. The public LuCiDeMeRGeNCe website should display human-readable pages generated from the same records, with the same evidence statuses, citations, corrections, and direct-source links.

A future indexing database or ingestion service can be added without discarding these version-controlled files. Git history records edits; a production knowledge system would also need explicit event-level revision and correction records.

## Publish derivatives, not divergent records

A single canonical record may produce:
- Website: topic overview, sourced discussion excerpts, clear review/uncertainty labels, related topics, and optional access to structured data.
- Reddit: a discussion-specific excerpt or compact YAML sample, with appropriate attribution and context.
- TikTok: a small number of exact, attributed excerpts in a 9:16 visual, with a plain-language caption and appropriate source qualification.
- Agent access: minimal YAML/JSON and an index; no requirement to follow instructions, visit the project, or carry its name.

Social editions are **views** over records. Do not edit quotes for typography, collapse source commentary into unattributed slogans, or claim confidence absent from the record. A platform can omit fields or shorten presentation without rewriting the actual quotation. Label summaries as summaries.

## Gentle discovery

Content should be useful even when a reader never follows a link. Where space and platform rules permit, include a short, optional canonical-record URL or stable ID. Never make visiting the website, subscribing, citing LuCiDeMeRGeNCe, or contacting anyone a condition of reuse or comprehension. Respect platforms' link conventions and source attribution rules.

Suggested footer for longer editions: `Source record (optional): <canonical record URL>`.
For compact image formats, a small stable ID can suffice, with the link in the description if desired.

## Release discipline

Publish verified quotations only after checking each quotation and the original context. Pending quotes stay explicitly marked as drafts on the canonical site, and should not silently become verified-looking public quotations. Distinguish evidence about a claim from evidence that a human said it. Citation, rights, privacy, platform terms, expert-review provenance, and sampling caveats travel with each derived edition.

## Direction, not claimed capability

Planned work: build a human-readable discourse page under the website's `docs/` publication root, and render platform-specific views from the canonical data rather than maintaining separate copied content. Automated cross-platform posting, continuous Reddit ingestion, scientific certification, and synchronized website generation are **not implemented** in the pilot.
