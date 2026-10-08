# API

## app.py

### index (method) `def index()`
- Defined: `app.py:24`
- Depends on: `lazyencoder_decoder.py`

### add_security_headers (method) `def add_security_headers(response)`
- Defined: `app.py:46`
- Depends on: `lazyencoder_decoder.py`

## lazyencoder_decoder.py

### base64_encode (function) `def base64_encode(data)`
- Defined: `lazyencoder_decoder.py:3`
- Imported by: `app.py`

### base64_decode (function) `def base64_decode(data)`
- Defined: `lazyencoder_decoder.py:6`
- Imported by: `app.py`

### caesar_cipher (function) `def caesar_cipher(text, shift)`
- Defined: `lazyencoder_decoder.py:10`
- Imported by: `app.py`

### caesar_decipher (function) `def caesar_decipher(text, shift)`
- Defined: `lazyencoder_decoder.py:23`
- Imported by: `app.py`

### key_substitution (function) `def key_substitution(text, key)`
- Defined: `lazyencoder_decoder.py:26`
- Imported by: `app.py`

### key_substitution_reverse (function) `def key_substitution_reverse(text, key)`
- Defined: `lazyencoder_decoder.py:41`
- Imported by: `app.py`

### encode (function) `def encode(data, shift, key)`
- Defined: `lazyencoder_decoder.py:56`
- Imported by: `app.py`

### encode_string (function) `def encode_string(data, shift, key)`
- Defined: `lazyencoder_decoder.py:67`
- Imported by: `app.py`

### decode (function) `def decode(data, shift, key)`
- Defined: `lazyencoder_decoder.py:73`
- Imported by: `app.py`

### decode_string (function) `def decode_string(data, shift, key)`
- Defined: `lazyencoder_decoder.py:84`
- Imported by: `app.py`
