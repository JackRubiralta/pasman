from secret import *
from encryption import *
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64

class Vault:
    def __init__(self, password: str) -> None:
        self.cSalt: bytes = generate_salt()
        self.cVerifier = encrypt(b"entered-master-correct", self.hash_password(password), b"salty-salt", b"peppery-pepper")

        self.pepper: bytes = generate_pepper()
       
        self.secrets: dict = {}

    def hash_password(self, password: str) -> bytes: # maybe move to encryption.py instead to clean up imports
        kdf = Scrypt(self.cSalt, 32, 2**14, 8, 1)
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def verify_key(self, key: bytes) -> bool:
        try:
            if decrypt(self.cVerifier, key, b"salty-salt", b"peppery-pepper") == b"entered-master-correct":
                return True
        except:
            pass
        return False

    def add_secret(self, name: str, login: str, password: str, key: bytes) -> None:
        self.secrets[name] = Secret(login, password, key)

    def remove_secret(self, name: str, key: bytes) -> None:
        self.secrets.pop(name)

    def get_secret(self, name: str) -> Secret:
        return self.secrets[name]

vault = Vault("password123")

password_provided = input("Enter Key: ")
key = vault.hash_password(password_provided)
if not vault.verify_key(key):
    print("FAIL at password")

while True:
    action = input("pasman ").split(" ")
        
    match action:
        case ["add", name, login, password]:
            vault.add_secret(name, login, password, key)
        case ["remove", name]:
            vault.remove_secret(name, key)
        case ["edit", name, attribute, value]:
            setattr(vault[name], attribute, value)

    print(str(vault.secrets))

