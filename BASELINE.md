# Post-transfer publication and link-integrity baseline

**Checked:** 2026-11-08  
**Canonical repository:** https://github.com/LuCiDeMeRGeNCe/LuCiDeMeRGeNCe  
**Configured website:** https://lucidemergence.github.io/LuCiDeMeRGeNCe/  
**Repository default branch:** main  
**GitHub Pages publishing content:** docs/index.html

## Confirmed through the GitHub connection

- The public repository is owned by the LuCiDeMeRGeNCe organization, not the original individual account.
- Issues and Discussions are enabled. [Challenge 001](https://github.com/LuCiDeMeRGeNCe/LuCiDeMeRGeNCe/issues/2) and [Challenge 002](https://github.com/LuCiDeMeRGeNCe/LuCiDeMeRGeNCe/issues/3) are open and retain their content.
- GitHub Actions Pages build and deployment [run 42498218630](https://github.com/LuCiDeMeRGeNCe/LuCiDeMeRGeNCe/actions/runs/42498218630) completed successfully for the updated site on November 8, 2026. Both the build and deployment jobs reported success. The [link-integrity run 42498219030](https://github.com/LuCiDeMeRGeNCe/LuCiDeMeRGeNCe/actions/runs/42498219030) passed all 253 inspected references and the live HTTP smoke test.
- Active text entry points, agent instructions, project metadata, and issue #2 were updated to use the organization URL. The original account remains mentioned where it belongs in the historical record.
- The root and website agent indexes, website metadata, and sitemap identify the new canonical website and repository.

## Ongoing checks

The [link-health workflow](.github/workflows/link-health.yml) runs an [internal link checker](scripts/check_links.py) on pushes and pull requests, and a live website smoke test on pushes, every Monday, or when manually dispatched. The local check validates relative file targets, repository blob paths, HTML navigation anchors, canonical ownership, project JSON and sitemap XML. The live check tests the website home page, /llms.txt, /robots.txt and /sitemap.xml for nonempty HTTP 200 responses.

## Live publication check

On 2026-11-08, the [GitHub-hosted link-health run 42498219030](https://github.com/LuCiDeMeRGeNCe/LuCiDeMeRGeNCe/actions/runs/42498219030) confirmed nonempty HTTP 200 responses for the public homepage, /llms.txt, /robots.txt, and /sitemap.xml. It also passed 253 local reference checks. This was a separate HTTP verification from GitHub's successful Pages deployment.

**Verification boundary:** HTTP success does not prove complete visual compatibility across browsers or the current reachability of every third-party research citation. Those areas remain outside this smoke test. No claim is made that the collaboration method itself has been scientifically validated.

## Preservation

The historical record retains the original ownership and dated publication events. Existing research, authorship records, and fictional canon have not been rewritten to manufacture new provenance. This audit is about functionality and routing, not a scientific validation of the project's research proposals.
