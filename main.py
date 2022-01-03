from secret import *
from encryption import *
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64

class MasterKey:
    def __init__(self, password: str) -> None:
        self.cSalt: bytes = generate_salt()
        self.cVerifier = encrypt(b"entered-master-correct", self.hash_password(password), b"salty-salt", b"peppery-pepper")

    def hash_password(self, password: str) -> bytes: # maybe move to encryption.py instead to clean up imports
        kdf = Scrypt(self.cSalt, 32, 2**14, 8, 1)
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def verify_key(self, key: bytes) -> bool:
        try:
            if decrypt(self.cVerifier, key, b"salty-salt", b"peppery-pepper") == b"entered-master-correct":
                return True
        except:
            return False
        return False

class Vault:
    def __init__(self) -> None:
        self.secrets = []
        
    def get(self, name: str, mkey: bytes):
        for secret in self.secrets:
            if secret.get_name(mkey) == name:
                return secret

    def add(self, name: str, login: str, password: str, mkey: bytes):
        self.secrets.append(Secret(name, login, password, mkey))
    
    def pop(self, name: str, mkey: bytes):
        self.secrets.remove(self.get(name, mkey))

    def edit(self, name: str, attribute: str, new: str ,mkey: bytes):
        getattr(self.get(name, mkey), "set_" + attribute)(new, mkey)



    




master_key = MasterKey("password123")
vault = Vault()

password_provided = input("Enter Key: ")
key = master_key.hash_password(password_provided)
if not master_key.verify_key(key):
    print("FAIL at password")

while True:
    action = input("pasman ").split(" ")
        
    match action:
        case ["add", name, login, password]:
            vault.add(name, login, password, key)
        case ["remove", name]:
            vault.pop(name, key)
        case ["edit", name, attribute, new]:
            vault.edit(name, attribute, new, key)

    print(vault.secrets[0].to_str(key))


    
    
