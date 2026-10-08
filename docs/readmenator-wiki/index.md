# Second Brain

*Last synthesized: 2026-10-07 | 2 files | 1 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `lazyencoder_decoder.py`, `app.py`. Architecturally it is 2 layers, dominant presentation (1 files) across 1 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Communities are self-contained in the resolved import graph; no cross-boundary bridges were recorded.

Open work clusters around documentation (0% file coverage), 0 security findings, 0 taint paths, and 4 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 2 |
| Symbols | 13 |
| Resolved imports | 1 |
| Languages | py |
| Communities | 1 |
| Doc coverage | 0% (0/2 files) |
| Security findings | 0 |
| Estimated read cost | ~550 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target readmenator_LazyOwnEncoderDecoder_qbvd90xl
```

## Concept Wiki

- [root (2 files, cohesion 1.00)](./community_0_root.md)

## God Nodes

| File | Score |
|------|-------|
| `lazyencoder_decoder.py` | 3.0 |
| `app.py` | 2.3 |

## Strongest Connections

- No cross-community connections recorded.

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
