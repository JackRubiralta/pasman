from .secrets import *

class Vault:
    def __init__(self) -> None:
        self.secrets: list = []
        
    def get(self, name: str, mkey: bytes) -> Secret:
        for secret in self.secrets:
            if secret.get_name(mkey) == name:
                return secret

    def add(self, name: str, login: str, password: str, mkey: bytes) -> None:
        self.secrets.append(Secret(name, login, password, mkey))
    
    def pop(self, name: str, mkey: bytes) -> None:
        self.secrets.remove(self.get(name, mkey))

    def edit(self, name: str, attribute: str, new: str ,mkey: bytes) -> None:
        getattr(self.get(name, mkey), "set_" + attribute)(new, mkey)