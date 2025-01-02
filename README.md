# encrypt_URL
This script encrypts a URL using AES (Advanced Encryption Standard) in CBC (Cipher Block Chaining) mode
# URL Encryption and Decryption Script

This project provides a simple Python implementation to **encrypt** and **decrypt URLs** using the AES encryption algorithm in **CBC (Cipher Block Chaining)** mode. 

---

## Features

- Securely encrypts URLs with a randomly generated AES key.
- Encodes encrypted data in **Base64** format for safe storage or transmission.
- Decrypts the encrypted URLs using the same AES key.
- Utilizes **padding and initialization vectors (IV)** for secure encryption.

---

## How It Works

1. **Encryption**:
   - A random 16-byte AES key is generated.
   - The URL is encrypted using the AES key and an IV (Initialization Vector).
   - The IV is prepended to the encrypted data and encoded into a Base64 string.

2. **Decryption**:
   - The Base64 encoded data is decoded.
   - The IV is extracted, and the AES cipher is initialized.
   - The data is decrypted and unpadded to recover the original URL.

---

## Requirements

This project uses the `pycryptodome` library for encryption and decryption. To install it:

```bash
pip install pycryptodome
