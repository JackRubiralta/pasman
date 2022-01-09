from .secrets import *
import pickle

class Database:
    def __init__(self) -> None:
        self.database = {}

    def add(self, name: str, secret: Profile) -> None:
        self.database[name] = secret

    def pop(self, name: str) -> None: 
        del self.database[name]

    def get(self, name: str) -> Profile:
        return self.database[name]

    def names(self) -> list[str]:
        return self.database.keys()

def load_database(mKey: bytes) -> Database:
    with open("database.pkl", "rb") as database_file:
        vault = pickle.loads(pickle.load(database_file).decrypted(mKey, b"associated-pepper"))
        database_file.close()
    return vault

def update_database(database: Database, mKey: bytes) -> None:
    with open('database.pkl', 'wb') as database_file:
        pickle.dump(CipherText(pickle.dumps(database), mKey, b"associated-pepper"), database_file, pickle.HIGHEST_PROTOCOL)
        database_file.close()