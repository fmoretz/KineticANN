## ================ from PAD to SAD - secondary averaging ===============
import sqlite3
import pandas as pd
import os.path
import numpy as np
from colorama import Fore, Style

#Connection to the DB
try:
    # Make sure to find the file.db in the script directory
    BASE_DIR = os.path.dirname(os.path.abspath('biscuit.ipynb'))
    db_path = os.path.join(BASE_DIR, "substrates.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    print('\n -- second averaging process started --')
    print(f'source connection... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
    print(f'source connection... [{Fore.RED}DENIED{Style.RESET_ALL}]')
try:
    PAD           = pd.read_sql_query('SELECT * FROM PAD', conn, index_col='index')
    Manure_PAD    = pd.read_sql_query('SELECT * FROM PAD WHERE "Category" = "Manure"',             conn, index_col='index')
    AgriWaste_PAD = pd.read_sql_query('SELECT * FROM PAD WHERE "Category" = "Agricultural waste"', conn, index_col='index')
    OrgWaste_PAD  = pd.read_sql_query('SELECT * FROM PAD WHERE "Category" = "Organic waste"',      conn, index_col='index')
    Sludges_PAD   = pd.read_sql_query('SELECT * FROM PAD WHERE "Category" = "Sludges"',            conn, index_col='index')
    print(f'retrieving data... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'retrieving data... [{Fore.RED}DENIED{Style.RESET_ALL}]')

cols = list(PAD)
try:
    Manure_SAD    = {str(cols[i]): np.nanmean(Manure_PAD[cols[i]].tolist())    for i in range (2, len(cols))}
    AgriWaste_SAD = {str(cols[i]): np.nanmean(AgriWaste_PAD[cols[i]].tolist()) for i in range (2, len(cols))}
    OrgWaste_SAD  = {str(cols[i]): np.nanmean(OrgWaste_PAD[cols[i]].tolist())  for i in range (2, len(cols))}
    Sludges_SAD   = {str(cols[i]): np.nanmean(Sludges_PAD[cols[i]].tolist())   for i in range (2, len(cols))}
    print(f'categorization... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'categorization... [{Fore.RED}DENIED{Style.RESET_ALL}]')
try:
    Manure     = pd.DataFrame(Manure_SAD,    index=[0])
    AgriWaste  = pd.DataFrame(AgriWaste_SAD, index=[0])
    OrgWaste   = pd.DataFrame(OrgWaste_SAD,  index=[0])
    Sludges    = pd.DataFrame(Sludges_SAD,   index=[0])
    Manure.insert(   0, 'Category', 'Manure')
    AgriWaste.insert(0, 'Category', 'Agricultural waste')
    OrgWaste.insert( 0, 'Category', 'Organic waste')
    Sludges.insert(  0, 'Category', 'Sludges')
    print(f'database generation... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'database generation... [{Fore.RED}DENIED{Style.RESET_ALL}]')
try:
    SAD = pd.concat([Manure, AgriWaste, OrgWaste, Sludges], ignore_index=True)
    print(f'concatenation information... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'concatenation information... [{Fore.RED}DENIED{Style.RESET_ALL}]')
try:
    c.execute('DROP TABLE SAD;')
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='SAD' ''')
    if c.fetchone()[0]==1:
        print(f'SAD table exists, upload {Fore.RED}passed{Style.RESET_ALL}')
    else:
        SAD.to_sql('SAD', conn)
        print(f'update {Fore.GREEN}successful{Style.RESET_ALL}!')
        print(f'database upload... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'database upload... [{Fore.RED}DENIED{Style.RESET_ALL}]')
