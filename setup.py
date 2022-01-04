from master_key import *
import pickle
master_password = input("Enter master password: ")
master_key = MasterKey(master_password)

with open('master.pkl', 'wb') as database:
    pickle.dump(master_key, database, pickle.HIGHEST_PROTOCOL)


    
    