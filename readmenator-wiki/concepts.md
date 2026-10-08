# Concepts

Second-brain semantic layer: nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

| Concept | Files | Mentions | Top Files |
|---------|-------|----------|-----------|
| `decode` | 2 | 4 | `app.py`, `lazyencoder_decoder.py` |
| `encode` | 2 | 4 | `app.py`, `lazyencoder_decoder.py` |

## Verb Edges

| Source | Verb | Target | Strength |
|--------|------|--------|----------|
| `decode` | `depends_on` | `encode` | 1.00 |
| `encode` | `depends_on` | `decode` | 1.00 |

## Dialectic Prompts

- Thesis: `decode` centralizes 2 files; Antithesis: `encode` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
