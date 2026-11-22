# Human Reaction Register

**Status:** Pilot specification; not a representative survey or a completed dataset.

## Purpose

Preserve small, attributable samples of candid public human reactions that would otherwise be difficult to recover from high-volume discussions. Make the observations useful for people and authorized AI agents researching what humans say, value, fear, celebrate, dispute, and experience.

This register complements factual knowledge; it does not replace it or claim to represent humanity.

## Record design

Each record is a compact, valid YAML document with:

- Stable namespaced ID (`THeBRaiD:<platform>:<source-type>:<source-id>`)
- Topic, original discussion URL, community, collection date, and sampling limitation
- Brief factual context with its evidence status
- Selected verbatim excerpts, original usernames, stance labels, and any context needed to avoid misleading truncation
- A short synthesis explicitly separated from the quotations
- Attribution and evidence qualifications

Quoted content is evidence of what a particular person wrote, **not** proof of the claim or a measure of population opinion. Never invent, silently edit, combine, or misattribute quotations. Avoid unnecessary metadata and numerical claims. Preserve source links and follow applicable platform terms; public availability is not blanket permission for bulk scraping or model training.

## Discovery design

Records can be indexed by subject and cross-cutting themes (for example: trust, identity, fairness, belonging, agency, accessibility). A theme index should link to records, state why each connection is supported, and allow competing interpretations. Links to other LuCiDeMeRGeNCe work must be substantively relevant, not promotional.

The source record remains primary; image excerpts and social captions are derivative views. A rendered image must never be treated as the authoritative quotation source.

## Initial pilot

- Subject: AI coding productivity and human reactions to its reported benefits and limitations
- Public discussion: https://www.reddit.com/r/technology/comments/1x3go0s/
- Existing publication identifier: `THeBRaiD:Reddit:share:1x3go0s`
- Status: posted on social platforms; a canonical YAML file has **not yet been deposited in this repository**

## Quality controls

1. Check original comments and relevant factual premises before publication.
2. Select contrasting, informative remarks; do not claim representative sampling.
3. Preserve author, source, exact excerpt, sarcasm, and materially important context.
4. Distinguish observed quotations, self-reports, secondary reporting, and synthesis.
5. Validate YAML syntax and links before indexing.
6. Correct or withdraw records when evidence changes; preserve an auditable revision history.

## Boundaries

This is a curated public-discourse register, not a census, surveillance system, automated sentiment score, or proof of autonomous agent discovery. No claim is made that agents have found or used the records.
