from master_key import *
from vault import *

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


    
    
