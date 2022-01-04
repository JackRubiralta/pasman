import pickle
from src.master_key import *
from src.vault import *

master_password = input("Enter new master password: ")
master = MasterKey(master_password)
mKey = master.hash_password(master_password)

with open('master.pkl', 'wb') as database:
    pickle.dump(master, database, pickle.HIGHEST_PROTOCOL)
    database.close()

vault = Vault()

with open('database.pkl', 'wb') as database:
    pickle.dump(CipherText(pickle.dumps(vault), mKey, b"associated-pepper"), database, pickle.HIGHEST_PROTOCOL)
    database.close()