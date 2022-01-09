from src.master import *
from src.database import *
from src.secrets import *
from src.encryption import *
import os

master = load_master()
password_provided = input("Enter password: ")
mKey = master.hash_password(password_provided)
if not master.verify_key(mKey):
    print("Password is incorrect!")
    raise Exception

database = load_database(mKey)

os.system("cls")
while True:
    print()
    action = input("pasman ").split(" ")

    match action:
        case ["add", name, login, password]:
            database.add(name, Profile(login, password, mKey))
            update_database(database, mKey)
            print(f"Added {name} to vault")

        case ["pop", name]:
            database.pop(name)
            update_database(database, mKey)
            print(f"Removed {name} from vault")

        case ["list"]:
            for i, name in enumerate(database.names()):
                print(f"({i + 1}) {name}")

        case ["edit", name, attribute, new]: 
            secret = database.get(name)
            match attribute:
                case "login":
                    secret.set_login(new, mKey)
                case "password":
                    secret.set_password(new, mKey)
            update_database(database, mKey)
            print(f"Changed {attribute} of profile {name}")

        case ["read", name]:
            secret = database.get(name)
            print(f"Login: {secret.get_login(mKey)}")
            print(f"Password: {secret.get_password(mKey)}")
        
        case ["help"]:
            print("Commands:")
            print("add [name] [login] [password] - Add profile")
            print("edit [name] [attribute {login, password}] [new] - Edit profile data")
            print("pop [name] - Delete profile")
            print("read [name] - Get profile data")
            print("list - Get profile names")
    
