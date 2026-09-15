# Subsystem: root

## app.py
- Layer: presentation
- Language: py
- Symbols:
  - `EncodeDecodeForm` (class, line 9) `class EncodeDecodeForm(FlaskForm)`
  - `index` (method, line 24) `def index()`
  - `add_security_headers` (method, line 46) `def add_security_headers(response)`
- Depends on: `lazyencoder_decoder.py`

## lazyencoder_decoder.py
- Layer: utility
- Language: py
- Symbols:
  - `base64_encode` (function, line 3) `def base64_encode(data)`
  - `base64_decode` (function, line 6) `def base64_decode(data)`
  - `caesar_cipher` (function, line 10) `def caesar_cipher(text, shift)`
  - `caesar_decipher` (function, line 23) `def caesar_decipher(text, shift)`
  - `key_substitution` (function, line 26) `def key_substitution(text, key)`
  - `key_substitution_reverse` (function, line 41) `def key_substitution_reverse(text, key)`
  - `encode` (function, line 56) `def encode(data, shift, key)`
  - `encode_string` (function, line 67) `def encode_string(data, shift, key)`
  - `decode` (function, line 73) `def decode(data, shift, key)`
  - `decode_string` (function, line 84) `def decode_string(data, shift, key)`
- Imported by: `app.py`
