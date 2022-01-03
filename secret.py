from encryption import *

class Secret():
    def __init__(self, login: str, password: str, key: bytes):
        self.pepper: bytes = generate_pepper()
        self.set_login(login, key)
        self.set_password(password, key)
    
    """
    def set_name(self, name: str, key: bytes) -> None:
        self.name = Cipher(name.encode(), key, self.pepper)
    def get_name(self, key: bytes) -> str:
        return self.name.decrypted(key, self.pepper).decode()
    """

    def set_login(self, login: str, key: bytes) -> None:
        self.login = Cipher(login.encode(), key, self.pepper)
    def get_login(self, key: bytes) -> str:
        return self.login.decrypted(key, self.pepper).decode()

    def set_password(self, password: str, key: bytes) -> None:
        self.password = Cipher(password.encode(), key, self.pepper)
    def get_password(self, key: bytes) -> str:
        return self.password.decrypted(key, self.pepper).decode()

    def __repr__(self) -> str:
        return f"<Login='{self.login}', Password='{self.password}'>"


