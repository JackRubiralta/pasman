from src.master_key import *
from src.vault import *
from src.secrets import *
from src.encryption import *
import pickle


with open('master.pkl', 'rb') as master_file:
    master = pickle.load(master_file)

password_provided = input("Enter Key: ")
mKey = master.hash_password(password_provided)
if not master.verify_key(mKey):
    print("FAIL at password")
    raise Exception

try:
    with open('database.pkl', 'rb') as database:
        vault = pickle.loads(pickle.load(database).decrypted(mKey, b"associated-pepper"))
except:
    raise Exception



while True:
    action = input("pasman ").split(" ")
        
    match action:
        case ["add", name, login, password]:
            vault.add(name, login, password, mKey)
        case ["remove", name]:
            vault.pop(name, mKey)
        case ["edit", name, attribute, new]:
            vault.edit(name, attribute, new, mKey)
    for secret in vault.secrets:
        print(secret.to_str(mKey))
        print(secret)

    with open('database.pkl', 'wb') as database:
        pickle.dump(CipherText(pickle.dumps(vault), mKey, b"associated-pepper"), database, pickle.HIGHEST_PROTOCOL)
        database.close()
   