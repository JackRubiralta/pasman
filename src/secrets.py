from .encryption import *

class Profile:
    def __init__(self, login: str, password: str, mKey: bytes):
        self.associated: bytes = generate_associated()
        self.set_login(login, mKey)
        self.set_password(password, mKey)

    def set_login(self, login: str, mKey: bytes) -> None:
        self.login = CipherText(login.encode(), mKey, self.associated)
    def get_login(self, mKey: bytes) -> str:
        return self.login.decrypted(mKey, self.associated).decode()

    def set_password(self, password: str, mKey: bytes) -> None:
        self.password = CipherText(password.encode(), mKey, self.associated)
    def get_password(self, mKey: bytes) -> str:
        return self.password.decrypted(mKey, self.associated).decode()

    def __repr__(self) -> str:
        return f"<Login={self.login}, Password={self.password}>"

    def to_str(self, mKey: bytes) -> str:
        return f"<Login={self.get_login(mKey)}, Password={self.get_password(mKey)}>"