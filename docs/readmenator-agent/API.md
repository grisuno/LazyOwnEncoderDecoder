# API

## app.py
Depends on: `lazyencoder_decoder.py`
- `EncodeDecodeForm.index` (method) `app.py:24` `def index()`
- `EncodeDecodeForm.add_security_headers` (method) `app.py:46` `def add_security_headers(response)`

## lazyencoder_decoder.py
Imported by: `app.py`
- `base64_encode` (function) `lazyencoder_decoder.py:3` `def base64_encode(data)`
- `base64_decode` (function) `lazyencoder_decoder.py:6` `def base64_decode(data)`
- `caesar_cipher` (function) `lazyencoder_decoder.py:10` `def caesar_cipher(text, shift)`
- `caesar_decipher` (function) `lazyencoder_decoder.py:23` `def caesar_decipher(text, shift)`
- `key_substitution` (function) `lazyencoder_decoder.py:26` `def key_substitution(text, key)`
- `key_substitution_reverse` (function) `lazyencoder_decoder.py:41` `def key_substitution_reverse(text, key)`
- `encode` (function) `lazyencoder_decoder.py:56` `def encode(data, shift, key)`
- `encode_string` (function) `lazyencoder_decoder.py:67` `def encode_string(data, shift, key)`
- `decode` (function) `lazyencoder_decoder.py:73` `def decode(data, shift, key)`
- `decode_string` (function) `lazyencoder_decoder.py:84` `def decode_string(data, shift, key)`
