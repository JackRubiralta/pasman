from .encryption import *
import pickle

class Master:
    def __init__(self, password: str) -> None:
        self.cSalt: bytes = generate_salt()
        self.verifier: bytes = CipherText(b"entered-master-correct", self.hash_password(password), b"peppery-pepper")

    def verify_key(self, mKey: bytes) -> bool:
        try:
            if self.verifier.decrypted(mKey, b"peppery-pepper") == b"entered-master-correct":
                return True
        except Exception:
            return False
        return False

    def hash_password(self, password: str) -> bytes:
        return hash_bytes(password.encode(), self.cSalt)

def load_master() -> Master:
    with open("master.pkl", "rb") as master_file:
        master = pickle.load(master_file)
        master_file.close()
    return master