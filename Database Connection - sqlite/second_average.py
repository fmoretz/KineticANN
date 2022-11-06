import sqlite3
import pandas as pd
import os.path
import statistics as st

# ========== from PAD to SAD - secondary averaging ========== # 

#Connection to the DB
try:
    # Make sure to find the file.db in the script directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    db_path = os.path.join(BASE_DIR, "substrates.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    print('\n -- second averaging process started --')

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)

# retrieve categorical dataframes from PAD table    
PAD           = pd.read_sql_query('SELECT * FROM PAD', conn, index_col='index')
Manure_PAD    = pd.read_sql_query('SELECT * FROM PAD WHERE "Category" = "Manure"',             conn, index_col='index')
AgriWaste_PAD = pd.read_sql_query('SELECT * FROM PAD WHERE "Category" = "Agricultural waste"', conn, index_col='index')
OrgWaste_PAD  = pd.read_sql_query('SELECT * FROM PAD WHERE "Category" = "Organic waste"',      conn, index_col='index')
Sludges_PAD   = pd.read_sql_query('SELECT * FROM PAD WHERE "Category" = "Sludges"',            conn, index_col='index')

# data processing
cols = list(PAD)
Manure_SAD    = {str(cols[i]): st.mean(Manure_PAD[cols[i]].tolist())    for i in range (2, len(cols))}
AgriWaste_SAD = {str(cols[i]): st.mean(AgriWaste_PAD[cols[i]].tolist()) for i in range (2, len(cols))}
OrgWaste_SAD  = {str(cols[i]): st.mean(OrgWaste_PAD[cols[i]].tolist())  for i in range (2, len(cols))}
Sludges_SAD   = {str(cols[i]): st.mean(Sludges_PAD[cols[i]].tolist())   for i in range (2, len(cols))}

# SAD dataframe generation
Manure    = pd.DataFrame(Manure_SAD, index=[0])
Manure.insert(0, 'Category', 'Manure')
AgriWaste    = pd.DataFrame(AgriWaste_SAD, index=[0])
AgriWaste.insert(0, 'Category', 'Agricultural waste')
OrgWaste    = pd.DataFrame(OrgWaste_SAD, index=[0])
OrgWaste.insert(0, 'Category', 'Organic waste')
Sludges    = pd.DataFrame(Sludges_SAD, index=[0])
Sludges.insert(0, 'Category', 'Sludges')

# Dataframe join
SAD = pd.concat([Manure, AgriWaste, OrgWaste, Sludges], ignore_index=True)

# SAD tale upload/update
c.execute('DROP TABLE SAD;')
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='SAD' ''')
if c.fetchone()[0]==1:
	print('\nSAD table exists, upload passed')
else:
    SAD.to_sql('SAD', conn)
    print('\nSAD updated successfully')