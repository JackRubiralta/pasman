from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.fernet import Fernet
import base64
import os

SALT_SIZE = 32

def encrypt_bytes(text: bytes, key: bytes, salt: bytes, pepper: bytes) -> bytes:
    return Fernet(key).encrypt(text + salt + pepper)

def decrypt_bytes(text: bytes, key: bytes, salt: bytes, pepper: bytes) -> bytes:
    return Fernet(key).decrypt(text).replace(salt, b"").replace(pepper, b"")

def hash_bytes(text: bytes, salt: bytes) -> bytes:
    kdf = Scrypt(salt, SALT_SIZE, 2**14, 8, 1)
    return base64.urlsafe_b64encode(kdf.derive(text))

def generate_salt() -> bytes:
    return os.urandom(SALT_SIZE)

def generate_pepper() -> bytes:
    return os.urandom(32)

class Cipher():
    def __init__(self, text: bytes, mKey: bytes, salt: bytes, pepper: bytes) -> None:
        self.salt: bytes = salt
        self.text: bytes = encrypt_bytes(text, mKey, self.salt, pepper)

    def decrypted(self, mKey: bytes, pepper: bytes) -> bytes:
        return decrypt_bytes(self.text, mKey, self.salt, pepper)

    def __repr__(self) -> str:
        return f"Cipher<(text='{str(self.text)}', salt='{str(self.salt)}')>"
