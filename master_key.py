from encryption import *

class MasterKey:
    def __init__(self, password: str) -> None:
        self.cSalt: bytes = generate_salt()
        self.salt: bytes = generate_salt()
        
        self.verifier: bytes = Cipher(b"entered-master-correct", self.hash_password(password), self.salt, b"peppery-pepper")

    def verify_key(self, mKey: bytes) -> bool:
        try:
            if self.verifier.decrypted(mKey, b"peppery-pepper") == b"entered-master-correct":
                return True
        except Exception:
            return False
        return False

    def hash_password(self, password: str) -> bytes:
        return hash_bytes(password.encode(), self.cSalt)