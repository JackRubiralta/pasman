from encryption import *

# could make stuff that gets encrypted have its own salt

class Secret():
    def __init__(self, name: str, login: str, password: str, mKey: bytes):
        self.pepper: bytes = generate_pepper()
        self.set_name(name, mKey)
        self.set_login(login, mKey)
        self.set_password(password, mKey)

    def set_name(self, name: str, mKey: bytes) -> None:
        self.name = Cipher(name.encode(), mKey, self.pepper)
    def get_name(self, mKey: bytes) -> str:
        return self.name.decrypted(mKey, self.pepper).decode()

    def set_login(self, login: str, mKey: bytes) -> None:
        self.login = Cipher(login.encode(), mKey, self.pepper)
    def get_login(self, mKey: bytes) -> str:
        return self.login.decrypted(mKey, self.pepper).decode()

    def set_password(self, password: str, mKey: bytes) -> None:
        self.password = Cipher(password.encode(), mKey, self.pepper)
    def get_password(self, mKey: bytes) -> str:
        return self.password.decrypted(mKey, self.pepper).decode()

    def __repr__(self) -> str:
        return f"<Name='{self.name}', Login='{self.login}', Password='{self.password}'>"

    def to_str(self, mKey: bytes) -> str:
        return f"<Name='{self.get_name(mKey)}', Login='{self.get_login(mKey)}', Password='{self.get_password(mKey)}'>"


