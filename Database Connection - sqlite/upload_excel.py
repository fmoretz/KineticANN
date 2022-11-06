import pandas as pd
import sqlite3
import os

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

# SAD table
SAD   = pd.read_excel('./Database/SAD.xlsx')
PAD   = pd.read_excel('./Database/PAD.xlsx')
ComDB = pd.read_excel('./Database/Complete_Database.xlsx')

# upload table to database
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='SAD' ''')
if c.fetchone()[0]==1:
	print('\nSAD table exists, upload passed')
else:
    SAD.to_sql('SAD', conn)
    print('\nSAD uploaded successfully')
    

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='PAD' ''')
if c.fetchone()[0]==1:
	print('\nPAD table exists, upload passed')
else:
    PAD.to_sql('PAD', conn)
    print('\nPAD uploaded successfully')
    
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='ComDB' ''')
if c.fetchone()[0]==1:
	print('\nComDB table exists, upload passed')
else:
    ComDB.to_sql('ComDB', conn)
    print('\nComDB uploaded successfully')

## just-in-case queries
# c.execute('DROP TABLE SAD;')
# c.execute('DROP TABLE PAD;')
# c.execute('DROP TABLE ComDB;')

# save and close connection
conn.commit()
conn.close()