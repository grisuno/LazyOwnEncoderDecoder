# Concepts

Nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

- `decode` | files=2 | mentions=4 | `app.py`, `lazyencoder_decoder.py`
- `encode` | files=2 | mentions=4 | `app.py`, `lazyencoder_decoder.py`

## Verb Edges

- `decode` --depends_on--> `encode` (strength 1.00)
- `encode` --depends_on--> `decode` (strength 1.00)

## Dialectic

- Thesis: `decode` centralizes 2 files; Antithesis: `encode` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
