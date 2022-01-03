from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.fernet import Fernet
import base64
import os

SALT_SIZE = 32

def encrypt_bytes(cipher: bytes, key: bytes, salt: bytes, pepper: bytes) -> bytes:
    return Fernet(key).encrypt(cipher + salt + pepper)

def decrypt_bytes(cipher: bytes, key: bytes, salt: bytes, pepper: bytes) -> bytes:
    return Fernet(key).decrypt(cipher).replace(salt, b"").replace(pepper, b"")

def hash_bytes(cipher: bytes, salt: bytes) -> bytes:
    kdf = Scrypt(salt, SALT_SIZE, 2**14, 8, 1)
    return base64.urlsafe_b64encode(kdf.derive(cipher))

def generate_salt() -> bytes:
    return os.urandom(SALT_SIZE)

def generate_pepper() -> bytes:
    return os.urandom(32)

class Cipher():
    def __init__(self, cipher: bytes, mKey: bytes, salt: bytes, pepper: bytes) -> None:
        self.salt: bytes = salt
        self.cipher: bytes = encrypt_bytes(cipher, mKey, self.salt, pepper)

    def decrypted(self, mKey: bytes, pepper: bytes) -> bytes:
        return decrypt_bytes(self.cipher, mKey, self.salt, pepper)

    def __repr__(self) -> str:
        return f"Cipher<(cipher='{self.cipher}', salt='{self.salt}')>"
