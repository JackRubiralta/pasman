import pickle
from src.database import *
from src.master import Master
import pickle

if __name__ == "__main__":
    master_password = input("Enter new master password: ")
    master = Master(master_password)
    mKey = master.hash_password(master_password)
    del master_password

    with open("master.pkl", "wb") as master_file:
        pickle.dump(master, master_file, pickle.HIGHEST_PROTOCOL)
        master_file.close()

    update_database(Database(), mKey)

    