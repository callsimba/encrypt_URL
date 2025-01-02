from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def decrypt_url(encrypted_url, key):
    encrypted_data = base64.b64decode(encrypted_url)
    iv = encrypted_data[:16]
    encrypted_message = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_message), AES.block_size)
    return decrypted_data.decode()

# Replace with your encrypted URL and key
encrypted_url = "PASTE_YOUR_ENCRYPTED_URL_HERE"
key = bytes.fromhex("PASTE_YOUR_KEY_HERE")

# Decrypt the URL
decrypted_url = decrypt_url(encrypted_url, key)
print(f"Decrypted URL: {decrypted_url}")
