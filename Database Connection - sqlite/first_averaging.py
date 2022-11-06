import sqlite3
import pandas as pd
import os.path
import statistics as st

# ========== from Complete Database (ComDB) to PAD - secondary averaging ========== # 

#Connection to the DB
try:
    # Make sure to find the file.db in the script directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    db_path = os.path.join(BASE_DIR, "substrates.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    print('\n -- first averaging process started --')

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)

# retrieve categorical dataframes from ComDB table    
ComDB = pd.read_sql_query('SELECT * FROM ComDB', conn, index_col='index')

# Manure category
Dairy_Manure_ComDB   = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Dairy manure"',   conn, index_col='index')
Goat_Manure_ComDB    = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Goat manure"',    conn, index_col='index')
Chicken_Manure_ComDB = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Chicken manure"', conn, index_col='index')
Sheep_Manure_ComDB   = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Sheep manure"',   conn, index_col='index')
Pig_Manure_ComDB     = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Pig manure"',     conn, index_col='index')
Sow_Manure_ComDB     = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Sow manure"',     conn, index_col='index')
Chicken_Litter_ComDB = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Chicken litter"', conn, index_col='index')

# Agricultural waste category
Straw_ComDB        = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Straw"',                 conn, index_col='index')
Rice_Husk_ComDB    = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Rice husk"',             conn, index_col='index')
Sugar_Beet_ComDB   = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Sugar beet byproducts"', conn, index_col='index')
Dry_Grass_ComDB    = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Dry grass"',             conn, index_col='index')
Maize_ComDB        = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Maize"',                 conn, index_col='index')
Raw_Potato_ComDB   = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Row Potato"',            conn, index_col='index')
Potato_Waste_ComDB = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Potato Waste"',          conn, index_col='index')
Yard_Waste_ComDB   = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Yard Waste"',            conn, index_col='index')
Bamboo_ComDB       = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Bamboo"',                conn, index_col='index')

# Organic waste category
Food_Waste_ComDB      = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Food waste"',                  conn, index_col='index')
Fruit_Veggie_ComDB    = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Fruit and vegetables waste "', conn, index_col='index')
Whey_ComDB            = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Whey"',                        conn, index_col='index')
OFMSW_ComDB           = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "OFMSW"',                       conn, index_col='index')
Fish_Waste_ComDB      = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Fish waste"',                  conn, index_col='index')
Slaughter_Res_ComDB   = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Slaughter residue"',           conn, index_col='index')
Vinegar_Res_ComDB     = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Vinegar residue"',             conn, index_col='index')
Precooked_Waste_ComDB = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Precooked waste"',             conn, index_col='index')
Exhaust_Oil_ComDB     = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Exhaust Kitchen Oil"',         conn, index_col='index')

# Sludges category
Sewage_ComDB   = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Sewage sludge"',         conn, index_col='index')
Food_Ind_ComDB = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Food industry sludges"', conn, index_col='index')

# # data processing
# cols = list(ComDB)
# Manure_SAD    = {str(cols[i]): st.mean(Manure_PAD[cols[i]].tolist())    for i in range (2, len(cols))}
# AgriWaste_SAD = {str(cols[i]): st.mean(AgriWaste_PAD[cols[i]].tolist()) for i in range (2, len(cols))}
# OrgWaste_SAD  = {str(cols[i]): st.mean(OrgWaste_PAD[cols[i]].tolist())  for i in range (2, len(cols))}
# Sludges_SAD   = {str(cols[i]): st.mean(Sludges_PAD[cols[i]].tolist())   for i in range (2, len(cols))}

# # SAD dataframe generation
# Manure    = pd.DataFrame(Manure_SAD, index=[0])
# Manure.insert(0, 'Category', 'Manure')
# AgriWaste    = pd.DataFrame(AgriWaste_SAD, index=[0])
# AgriWaste.insert(0, 'Category', 'Agricultural waste')
# OrgWaste    = pd.DataFrame(OrgWaste_SAD, index=[0])
# OrgWaste.insert(0, 'Category', 'Organic waste')
# Sludges    = pd.DataFrame(Sludges_SAD, index=[0])
# Sludges.insert(0, 'Category', 'Sludges')

# # Dataframe join
# SAD = pd.concat([Manure, AgriWaste, OrgWaste, Sludges], ignore_index=True)

# # SAD tale upload/update
# c.execute('DROP TABLE SAD;')
# c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='SAD' ''')
# if c.fetchone()[0]==1:
# 	print('\nSAD table exists, upload passed')
# else:
#     SAD.to_sql('SAD', conn)
#     print('\nSAD updated successfully')