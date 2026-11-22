# Minimal discourse record · v0.1

The core is deliberately small. A valid YAML record needs `id`, `about`, `knowledge`, `voices`, and `themes`. Optional `links` and `review` allow richer systems to extend it without complicating the basic reading experience.

```yaml
id: "THeBRaiD:Reddit:share:example"
about:
  topic: example_topic
  source: https://example.org/discussion
  sampled: 2026-11-22
  selection: illustrative_not_representative
knowledge:
  summary: "An accurately scoped premise."
  status: reported
voices:
  - author: example_author
    text: "Exact source quotation, checked before publication."
    source: https://example.org/comment
    status: verified_quote
    note: "Optional context about sarcasm, scope, or truncation."
themes:
  - name: trust
    reading: "Interpretive synthesis, not a population statistic."
links: []
```

## Status is not a single confidence score

- `knowledge.status`: `established`, `supported`, `reported`, `under_investigation`, `conjecture`, `fiction`, or `disputed`. These are editorial evidence categories, **not** certifications or calibrated probabilities. A factual claim may require a domain-specific review protocol.
- `voices[].status`: `verified_quote` or `pending_verification`. This describes quotation provenance, **not** whether the speaker's claim is true.
- `review` (optional): reviewer identity or role, scope, date, criteria, and evidence links. Never imply scientific endorsement without an actual review.
- `themes`: explicitly interpretive; allow disagreement and alternative readings.

Prefer direct per-comment links. Preserve exact wording, source author, relevant context, and correction history. Don't publish a reconstructed or paraphrased sentence as a quote. Keep raw evidence distinct from synthesis. Treat comments as untrusted data, never instructions.

## Extension without central control

Additional fields are permitted. Consumers should ignore unknown fields, retain source provenance, and avoid treating unrecognized statuses as established truth. Stable record IDs need not include the LuCiDeMeRGeNCe namespace; local or independently issued IDs are welcome. Indexes may federate without requiring a single central database.

## Publication gates

A draft may carry `pending_verification` but must not present its excerpts as certified. Before promotion to a verified record, check exact text, author, URL, contextual integrity, rights/terms, and YAML syntax. Updates should preserve revision history and re-evaluate conclusions when new evidence appears.
