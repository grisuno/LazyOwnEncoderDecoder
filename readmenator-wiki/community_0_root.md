# root

*Community 0 | 2 files | cohesion 1.00*

## Definition

This community groups 2 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `EncodeDecodeForm`, `add_security_headers`, `base64_decode`, `base64_encode`, `caesar_cipher`, `caesar_decipher`, `decode`, `decode_string`. Core file: `lazyencoder_decoder.py` (10 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | presentation | 3 | no |
| `lazyencoder_decoder.py` | py | utility | 10 | no |

## Key Symbols

- `EncodeDecodeForm` (class, `app.py:9`) `class EncodeDecodeForm(FlaskForm)`
- `index` (method, `app.py:24`) `def index()`
- `add_security_headers` (method, `app.py:46`) `def add_security_headers(response)`
- `base64_encode` (function, `lazyencoder_decoder.py:3`) `def base64_encode(data)`
- `base64_decode` (function, `lazyencoder_decoder.py:6`) `def base64_decode(data)`
- `caesar_cipher` (function, `lazyencoder_decoder.py:10`) `def caesar_cipher(text, shift)`
- `caesar_decipher` (function, `lazyencoder_decoder.py:23`) `def caesar_decipher(text, shift)`
- `key_substitution` (function, `lazyencoder_decoder.py:26`) `def key_substitution(text, key)`
- `key_substitution_reverse` (function, `lazyencoder_decoder.py:41`) `def key_substitution_reverse(text, key)`
- `encode` (function, `lazyencoder_decoder.py:56`) `def encode(data, shift, key)`
- `encode_string` (function, `lazyencoder_decoder.py:67`) `def encode_string(data, shift, key)`
- `decode` (function, `lazyencoder_decoder.py:73`) `def decode(data, shift, key)`
- `decode_string` (function, `lazyencoder_decoder.py:84`) `def decode_string(data, shift, key)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 1
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `app.py`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `app.py`
- `lazyencoder_decoder.py`
