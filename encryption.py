from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.fernet import Fernet
import os

def encrypt(cipher: bytes, key: bytes, salt: bytes, pepper: bytes) -> bytes:
    return Fernet(key).encrypt(cipher + salt + pepper)

def decrypt(cipher: bytes, key: bytes, salt: bytes, pepper: bytes) -> bytes:
    return Fernet(key).decrypt(cipher).replace(salt, b"").replace(pepper, b"")

def generate_salt() -> bytes:
    return os.urandom(32)

def generate_pepper() -> bytes:
    return os.urandom(32)

class Cipher():
    def __init__(self, cipher: bytes, mKey: bytes, pepper: bytes) -> None:
        self.salt: bytes = generate_salt()
        self.cipher: bytes = encrypt(cipher, mKey, self.salt, pepper)

    def decrypted(self, mKey: bytes, pepper: bytes) -> bytes:
        return decrypt(self.cipher, mKey, self.salt, pepper)

    def __repr__(self) -> str:
        return self.cipher.decode()
