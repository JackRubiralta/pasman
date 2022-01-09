import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import os
import base64


def generate_nonce() -> bytes:
    return os.urandom(16)

def generate_associated() -> bytes:
    return os.urandom(32)

def generate_salt() -> bytes:
    return os.urandom(32)

def hash_bytes(plaintext: bytes, salt: bytes) -> bytes:
    return Scrypt(salt, 32, 2**14, 8, 1).derive(plaintext)

def digest_key(key: bytes, salt: bytes) -> bytes:
    return hash_bytes(key, salt)

def encrypt_bytes(plaintext: bytes, key: bytes, nonce: bytes, salt: bytes, associated: bytes) -> bytes:
    return AESGCM(digest_key(key, salt)).encrypt(nonce, plaintext, associated)

def decrypt_bytes(ciphertext: bytes, key: bytes, nonce: bytes, salt: bytes, associated: bytes) -> bytes:
    return AESGCM(digest_key(key, salt)).decrypt(nonce, ciphertext, associated)

class CipherText: # maybe make sub class of bytes
    def __init__(self, plaintext: bytes, mKey: bytes, associated: bytes) -> None:
        self.salt: bytes = generate_salt()
        self.nonce: bytes = generate_nonce()
        self.ciphertext: bytes = encrypt_bytes(plaintext, mKey, self.nonce, self.salt, associated)

    def decrypted(self, mKey: bytes, associated: bytes) -> bytes:
        return decrypt_bytes(self.ciphertext, mKey, self.nonce, self.salt, associated)

    def __repr__(self) -> str:
        return base64.urlsafe_b64encode(self.ciphertext).decode()

