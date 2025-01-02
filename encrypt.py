from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import os

def encrypt_url(url, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(url.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_data).decode()

# Generate a random AES key
key = os.urandom(16)
print(f"Encryption Key (Save this in your loader!): {key.hex()}")

# URL to encrypt
url = "https://example.com/resource"
encrypted_url = encrypt_url(url, key)
print(f"Encrypted URL: {encrypted_url}")
