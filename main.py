from master_key import *
from vault import *
import pickle


with open('master.pkl', 'rb') as database:
    master_key = pickle.load(database)


  

password_provided = input("Enter Key: ")
key = master_key.hash_password(password_provided)
if not master_key.verify_key(key):
    print("FAIL at password")



try:
    with open('database.pkl', 'rb') as database:
        vault = pickle.loads(pickle.load(database).decrypted(key, b"peppery-pepper"))
except:
    print("error")
    vault = Vault()

while True:
    action = input("pasman ").split(" ")
        
    match action:
        case ["add", name, login, password]:
            vault.add(name, login, password, key)
        case ["remove", name]:
            vault.pop(name, key)
        case ["edit", name, attribute, new]:
            vault.edit(name, attribute, new, key)
    for secret in vault.secrets:
        print(secret.to_str(key))
    with open('database.pkl', 'wb') as database:
        pickle.dump(Cipher(pickle.dumps(vault), key, b'salt-salt', b"peppery-pepper"), database, pickle.HIGHEST_PROTOCOL)


    
    
