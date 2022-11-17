import sqlite3
import pandas as pd
import os.path
import numpy as np
import statistics as st
from colorama import Fore, Style

## ========= from Complete Database (ComDB) to PAD - first averaging =========
#Connection to the DB
try:
    # Make sure to find the file.db in the script directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "substrates.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    print('\n -- primary averaging process started --')
    print(f'source connection... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
    print(f'source connection... [{Fore.RED}DENIED{Style.RESET_ALL}]')
try:
    ComDB = pd.read_sql_query('SELECT * FROM ComDB', conn, index_col='index')
    print(f'retrieving data... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'retrieving data... [{Fore.RED}DENIED{Style.RESET_ALL}]')
try:
    Dairy_Manure_ComDB    = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Dairy manure"',                 conn, index_col='index')
    Goat_Manure_ComDB     = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Goat manure"',                  conn, index_col='index')
    Chicken_Manure_ComDB  = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Chicken manure"',               conn, index_col='index')
    Sheep_Manure_ComDB    = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Sheep manure"',                 conn, index_col='index')
    Pig_Manure_ComDB      = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Pig manure"',                   conn, index_col='index')
    Sow_Manure_ComDB      = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Sow manure"',                   conn, index_col='index')
    Chicken_Litter_ComDB  = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Chicken litter"',               conn, index_col='index')
    Straw_ComDB           = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Straw"',                        conn, index_col='index')
    Rice_Husk_ComDB       = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Rice husk"',                    conn, index_col='index')
    Sugar_Beet_ComDB      = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Sugar Beet Byproducts"',        conn, index_col='index')
    Dry_Grass_ComDB       = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Dry grass "',                   conn, index_col='index')
    Maize_ComDB           = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Maize Waste"',                  conn, index_col='index')
    Potato_Waste_ComDB    = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Potato Waste"',                 conn, index_col='index')
    Yard_Waste_ComDB      = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Yard waste"',                   conn, index_col='index')
    Bamboo_ComDB          = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Bamboo"',                       conn, index_col='index')
    Food_Waste_ComDB      = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Food waste"',                   conn, index_col='index')
    Fruit_Veggie_ComDB    = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Fruit and veg food waste"',     conn, index_col='index')
    OFMSW_ComDB           = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "OFMSW"',                        conn, index_col='index')
    Fish_Waste_ComDB      = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Fish waste"',                   conn, index_col='index')
    Slaughter_Res_ComDB   = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Slaughter residue"',            conn, index_col='index')
    Vinegar_Res_ComDB     = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Vinegar residue"',              conn, index_col='index')
    Precooked_Waste_ComDB = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Precooked carbs-based waste "', conn, index_col='index')
    Exhaust_Oil_ComDB     = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Exhaust kitchen oil"',          conn, index_col='index')
    Sewage_ComDB          = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Sewage sludge"',                conn, index_col='index')
    Food_Ind_ComDB        = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Food industry sludges"',        conn, index_col='index')
    print(f'categorization... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'categorization... [{Fore.RED}DENIED{Style.RESET_ALL}]')
cols = list(ComDB)

try:
    Dairy_Manure_ComDB    = Dairy_Manure_ComDB.drop(   [cols[0], cols[1]], axis=1).T.to_numpy()
    Goat_Manure_ComDB     = Goat_Manure_ComDB.drop(    [cols[0], cols[1]], axis=1).T.to_numpy()
    Chicken_Manure_ComDB  = Chicken_Manure_ComDB.drop( [cols[0], cols[1]], axis=1).T.to_numpy()
    Sheep_Manure_ComDB    = Sheep_Manure_ComDB.drop(   [cols[0], cols[1]], axis=1).T.to_numpy()
    Pig_Manure_ComDB      = Pig_Manure_ComDB.drop(     [cols[0], cols[1]], axis=1).T.to_numpy()
    Sow_Manure_ComDB      = Sow_Manure_ComDB.drop(     [cols[0], cols[1]], axis=1).T.to_numpy()
    Chicken_Litter_ComDB  = Chicken_Litter_ComDB.drop( [cols[0], cols[1]], axis=1).T.to_numpy()
    Straw_ComDB           = Straw_ComDB.drop(          [cols[0], cols[1]], axis=1).T.to_numpy()
    Rice_Husk_ComDB       = Rice_Husk_ComDB.drop(      [cols[0], cols[1]], axis=1).T.to_numpy()
    Sugar_Beet_ComDB      = Sugar_Beet_ComDB.drop(     [cols[0], cols[1]], axis=1).T.to_numpy()
    Dry_Grass_ComDB       = Dry_Grass_ComDB.drop(      [cols[0], cols[1]], axis=1).T.to_numpy()
    Maize_ComDB           = Maize_ComDB.drop(          [cols[0], cols[1]], axis=1).T.to_numpy()
    Potato_Waste_ComDB    = Potato_Waste_ComDB.drop(   [cols[0], cols[1]], axis=1).T.to_numpy()
    Yard_Waste_ComDB      = Yard_Waste_ComDB.drop(     [cols[0], cols[1]], axis=1).T.to_numpy()
    Bamboo_ComDB          = Bamboo_ComDB.drop(         [cols[0], cols[1]], axis=1).T.to_numpy()
    Food_Waste_ComDB      = Food_Waste_ComDB.drop(     [cols[0], cols[1]], axis=1).T.to_numpy()
    Fruit_Veggie_ComDB    = Fruit_Veggie_ComDB.drop(   [cols[0], cols[1]], axis=1).T.to_numpy()
    OFMSW_ComDB           = OFMSW_ComDB.drop(          [cols[0], cols[1]], axis=1).T.to_numpy()
    Fish_Waste_ComDB      = Fish_Waste_ComDB.drop(     [cols[0], cols[1]], axis=1).T.to_numpy()
    Slaughter_Res_ComDB   = Slaughter_Res_ComDB.drop(  [cols[0], cols[1]], axis=1).T.to_numpy()
    Vinegar_Res_ComDB     = Vinegar_Res_ComDB.drop(    [cols[0], cols[1]], axis=1).T.to_numpy()
    Precooked_Waste_ComDB = Precooked_Waste_ComDB.drop([cols[0], cols[1]], axis=1).T.to_numpy()
    Exhaust_Oil_ComDB     = Exhaust_Oil_ComDB.drop(    [cols[0], cols[1]], axis=1).T.to_numpy()
    Sewage_ComDB          = Sewage_ComDB.drop(         [cols[0], cols[1]], axis=1).T.to_numpy()
    Food_Ind_ComDB        = Food_Ind_ComDB.drop(       [cols[0], cols[1]], axis=1).T.to_numpy()
    print(f'data extraction... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'data extraction... [{Fore.RED}DENIED{Style.RESET_ALL}]')
cols = cols[2:]
try:
    Dairy_Manure    = {str(cols[i]): np.nanmean(Dairy_Manure_ComDB[i],    dtype='float32') for i in range(0, len(cols))}
    Goat_Manure     = {str(cols[i]): np.nanmean(Goat_Manure_ComDB[i],     dtype='float32') for i in range(0, len(cols))}
    Chicken_Manure  = {str(cols[i]): np.nanmean(Chicken_Manure_ComDB[i],  dtype='float32') for i in range(0, len(cols))}
    Sheep_Manure    = {str(cols[i]): np.nanmean(Sheep_Manure_ComDB[i],    dtype='float32') for i in range(0, len(cols))}
    Pig_Manure      = {str(cols[i]): np.nanmean(Pig_Manure_ComDB[i],      dtype='float32') for i in range(0, len(cols))}
    Sow_Manure      = {str(cols[i]): np.nanmean(Sow_Manure_ComDB[i],      dtype='float32') for i in range(0, len(cols))}
    Chicken_Litter  = {str(cols[i]): np.nanmean(Chicken_Litter_ComDB[i],  dtype='float32') for i in range(0, len(cols))}
    Straw           = {str(cols[i]): np.nanmean(Straw_ComDB[i],           dtype='float32') for i in range(0, len(cols))}
    Rice_Husk       = {str(cols[i]): np.nanmean(Rice_Husk_ComDB[i],       dtype='float32') for i in range(0, len(cols))}
    Sugar_Beet      = {str(cols[i]): np.nanmean(Sugar_Beet_ComDB[i],      dtype='float32') for i in range(0, len(cols))}
    Dry_Grass       = {str(cols[i]): np.nanmean(Dry_Grass_ComDB[i],       dtype='float32') for i in range(0, len(cols))}
    Maize           = {str(cols[i]): np.nanmean(Maize_ComDB[i],           dtype='float32') for i in range(0, len(cols))}
    Potato_Waste    = {str(cols[i]): np.nanmean(Potato_Waste_ComDB[i],    dtype='float32') for i in range(0, len(cols))}
    Yard_Waste      = {str(cols[i]): np.nanmean(Yard_Waste_ComDB[i],      dtype='float32') for i in range(0, len(cols))}
    Bamboo          = {str(cols[i]): np.nanmean(Bamboo_ComDB[i],          dtype='float32') for i in range(0, len(cols))}
    Food_Waste      = {str(cols[i]): np.nanmean(Food_Waste_ComDB[i],      dtype='float32') for i in range(0, len(cols))}
    Fruit_Veggie    = {str(cols[i]): np.nanmean(Fruit_Veggie_ComDB[i],    dtype='float32') for i in range(0, len(cols))}
    OFMSW           = {str(cols[i]): np.nanmean(OFMSW_ComDB[i],           dtype='float32') for i in range(0, len(cols))}
    Fish_Waste      = {str(cols[i]): np.nanmean(Fish_Waste_ComDB[i],      dtype='float32') for i in range(0, len(cols))}
    Slaughter_Res   = {str(cols[i]): np.nanmean(Slaughter_Res_ComDB[i],   dtype='float32') for i in range(0, len(cols))}
    Vinegar_Res     = {str(cols[i]): np.nanmean(Vinegar_Res_ComDB[i],     dtype='float32') for i in range(0, len(cols))}
    Precooked_Waste = {str(cols[i]): np.nanmean(Precooked_Waste_ComDB[i], dtype='float32') for i in range(0, len(cols))}
    Exhaust_Oil     = {str(cols[i]): np.nanmean(Exhaust_Oil_ComDB[i],     dtype='float32') for i in range(0, len(cols))}
    Sewage          = {str(cols[i]): np.nanmean(Sewage_ComDB[i],          dtype='float32') for i in range(0, len(cols))}
    Food_Ind        = {str(cols[i]): np.nanmean(Food_Ind_ComDB[i],        dtype='float32') for i in range(0, len(cols))}
    print(f'category averaging... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'category averaging... [{Fore.RED}DENIED{Style.RESET_ALL}]')
try:
    Dairy_Manure    = pd.DataFrame(Dairy_Manure   , index=[0])
    Goat_Manure     = pd.DataFrame(Goat_Manure    , index=[0])
    Chicken_Manure  = pd.DataFrame(Chicken_Manure , index=[0])
    Sheep_Manure    = pd.DataFrame(Sheep_Manure   , index=[0])
    Pig_Manure      = pd.DataFrame(Pig_Manure     , index=[0])
    Sow_Manure      = pd.DataFrame(Sow_Manure     , index=[0])
    Chicken_Litter  = pd.DataFrame(Chicken_Litter , index=[0])
    Straw           = pd.DataFrame(Straw          , index=[0])
    Rice_Husk       = pd.DataFrame(Rice_Husk      , index=[0])
    Sugar_Beet      = pd.DataFrame(Sugar_Beet     , index=[0])
    Dry_Grass       = pd.DataFrame(Dry_Grass      , index=[0])
    Maize           = pd.DataFrame(Maize          , index=[0])
    Potato_Waste    = pd.DataFrame(Potato_Waste   , index=[0])
    Yard_Waste      = pd.DataFrame(Yard_Waste     , index=[0])
    Bamboo          = pd.DataFrame(Bamboo         , index=[0])
    Food_Waste      = pd.DataFrame(Food_Waste     , index=[0])
    Fruit_Veggie    = pd.DataFrame(Fruit_Veggie   , index=[0])
    OFMSW           = pd.DataFrame(OFMSW          , index=[0])
    Fish_Waste      = pd.DataFrame(Fish_Waste     , index=[0])
    Slaughter_Res   = pd.DataFrame(Slaughter_Res  , index=[0])
    Vinegar_Res     = pd.DataFrame(Vinegar_Res    , index=[0])
    Precooked_Waste = pd.DataFrame(Precooked_Waste, index=[0])
    Exhaust_Oil     = pd.DataFrame(Exhaust_Oil    , index=[0])
    Sewage          = pd.DataFrame(Sewage         , index=[0])
    Food_Ind        = pd.DataFrame(Food_Ind       , index=[0])
    Dairy_Manure.insert(   0, 'Category', 'Dairy_Manure   ')
    Goat_Manure.insert(    0, 'Category', 'Goat_Manure    ')
    Chicken_Manure.insert( 0, 'Category', 'Chicken_Manure ')
    Sheep_Manure.insert(   0, 'Category', 'Sheep_Manure   ')
    Pig_Manure.insert(     0, 'Category', 'Pig_Manure     ')
    Sow_Manure.insert(     0, 'Category', 'Sow_Manure     ')
    Chicken_Litter.insert( 0, 'Category', 'Chicken_Litter ')
    Straw.insert(          0, 'Category', 'Straw          ')
    Rice_Husk.insert(      0, 'Category', 'Rice_Husk      ')
    Sugar_Beet.insert(     0, 'Category', 'Sugar_Beet     ')
    Dry_Grass.insert(      0, 'Category', 'Dry_Grass      ')
    Maize.insert(          0, 'Category', 'Maize          ')
    Potato_Waste.insert(   0, 'Category', 'Potato_Waste   ')
    Yard_Waste.insert(     0, 'Category', 'Yard_Waste     ')
    Bamboo.insert(         0, 'Category', 'Bamboo         ')
    Food_Waste.insert(     0, 'Category', 'Food_Waste     ')
    Fruit_Veggie.insert(   0, 'Category', 'Fruit_Veggie   ')
    OFMSW.insert(          0, 'Category', 'OFMSW          ')
    Fish_Waste.insert(     0, 'Category', 'Fish_Waste     ')
    Slaughter_Res.insert(  0, 'Category', 'Slaughter_Res  ')
    Vinegar_Res.insert(    0, 'Category', 'Vinegar_Res    ')
    Precooked_Waste.insert(0, 'Category', 'Precooked_Waste')
    Exhaust_Oil.insert(    0, 'Category', 'Exhaust_Oil    ')
    Sewage.insert(         0, 'Category', 'Sewage         ')
    Food_Ind.insert(       0, 'Category', 'Food_Ind       ')
    print(f'database generation... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'database generation... [{Fore.RED}DENIED{Style.RESET_ALL}]')
try:
    PAD = pd.concat(
        [ Dairy_Manure, Goat_Manure, Chicken_Manure, Sheep_Manure, Pig_Manure, Sow_Manure, Chicken_Litter, \
          Straw, Rice_Husk, Sugar_Beet, Dry_Grass, Maize, Potato_Waste, Yard_Waste, Bamboo, Food_Waste, \
          Fruit_Veggie, OFMSW, Fish_Waste, Slaughter_Res, Vinegar_Res, Precooked_Waste, Exhaust_Oil, Sewage, Food_Ind,
        ],
        ignore_index=True
        )
    print(f'concatenation information... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'concatenation information... [{Fore.RED}DENIED{Style.RESET_ALL}]')
try:
    c.execute('DROP TABLE PAD;')
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='PAD' ''')
    if c.fetchone()[0]==1:
        print(f'PAD table exists, upload {Fore.RED}passed{Style.RESET_ALL}')
    else:
        PAD.to_sql('PAD', conn)
        print(f'update {Fore.GREEN}successful{Style.RESET_ALL}!')
        print(f'database upload... [{Fore.GREEN}OK{Style.RESET_ALL}]')

except: print(f'database upload... [{Fore.RED}DENIED{Style.RESET_ALL}]')