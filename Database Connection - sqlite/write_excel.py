import pandas as pd
import sqlite3
import os
from colorama import Fore, Style

#Connection to the DB
try:
    # Make sure to find the file.db in the script directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    if os.path.isfile("./substrates.db") == True:
        pass
    else:
        os.system('touch substrates.db')

    db_path = os.path.join(BASE_DIR, "substrates.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    print('\nConnection Successfull!')

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)




except: print(f'writer engine... [{Fore.RED}DENIED{Style.RESET_ALL}]')

# load table table
try:
    PAD   = pd.read_sql_query('SELECT * FROM PAD',   conn, index_col='index')
    SAD   = pd.read_sql_query('SELECT * FROM SAD',   conn, index_col='index')
    ComDB = pd.read_sql_query('SELECT * FROM ComDB', conn, index_col='index')
    print(f'collecting tables... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'collecting tables... [{Fore.RED}DENIED{Style.RESET_ALL}]')

try:
        # writer for write the data into excel file
    SAD_path   = str(os.path.join(BASE_DIR, "./Database/SAD.csv"))
    PAD_path   = str(os.path.join(BASE_DIR, "./Database/PAD.csv"))
    ComDB_path = str(os.path.join(BASE_DIR, "./Database/Complete_Database.csv"))

    PAD.to_csv(  SAD_path)
    SAD.to_csv(  PAD_path)
    ComDB.to_csv(ComDB_path)
    print(f'download excel file... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'download excel file... [{Fore.RED}DENIED{Style.RESET_ALL}]')