import sqlite3
import pandas as pd
import os.path
import numpy as np
from colorama import Fore, Style
import os

def first_averagind():
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
        Blood_ComDB           = pd.read_sql_query('SELECT * FROM ComDB WHERE "Substrate" = "Blood"',                        conn, index_col='index')
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
        Blood_ComDB           = Blood_ComDB.drop(          [cols[0], cols[1]], axis=1).T.to_numpy()
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
        Blood           = {str(cols[i]): np.nanmean(Blood_ComDB[i],           dtype='float32') for i in range(0, len(cols))}
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
        Blood           = pd.DataFrame(Blood          , index=[0])
        Vinegar_Res     = pd.DataFrame(Vinegar_Res    , index=[0])
        Precooked_Waste = pd.DataFrame(Precooked_Waste, index=[0])
        Exhaust_Oil     = pd.DataFrame(Exhaust_Oil    , index=[0])
        Sewage          = pd.DataFrame(Sewage         , index=[0])
        Food_Ind        = pd.DataFrame(Food_Ind       , index=[0])

        # Substrate type insertion
        Dairy_Manure.insert(   0, 'Substrate', 'Dairy_Manure   ')
        Goat_Manure.insert(    0, 'Substrate', 'Goat_Manure    ')
        Chicken_Manure.insert( 0, 'Substrate', 'Chicken_Manure ')
        Sheep_Manure.insert(   0, 'Substrate', 'Sheep_Manure   ')
        Pig_Manure.insert(     0, 'Substrate', 'Pig_Manure     ')
        Sow_Manure.insert(     0, 'Substrate', 'Sow_Manure     ')
        Chicken_Litter.insert( 0, 'Substrate', 'Chicken_Litter ')
        Straw.insert(          0, 'Substrate', 'Straw          ')
        Rice_Husk.insert(      0, 'Substrate', 'Rice_Husk      ')
        Sugar_Beet.insert(     0, 'Substrate', 'Sugar_Beet     ')
        Dry_Grass.insert(      0, 'Substrate', 'Dry_Grass      ')
        Maize.insert(          0, 'Substrate', 'Maize          ')
        Potato_Waste.insert(   0, 'Substrate', 'Potato_Waste   ')
        Yard_Waste.insert(     0, 'Substrate', 'Yard_Waste     ')
        Bamboo.insert(         0, 'Substrate', 'Bamboo         ')
        Food_Waste.insert(     0, 'Substrate', 'Food_Waste     ')
        Fruit_Veggie.insert(   0, 'Substrate', 'Fruit_Veggie   ')
        OFMSW.insert(          0, 'Substrate', 'OFMSW          ')
        Fish_Waste.insert(     0, 'Substrate', 'Fish_Waste     ')
        Slaughter_Res.insert(  0, 'Substrate', 'Slaughter_Res  ')
        Blood.insert(          0, 'Substrate', 'Blood          ')
        Vinegar_Res.insert(    0, 'Substrate', 'Vinegar_Res    ')
        Precooked_Waste.insert(0, 'Substrate', 'Precooked_Waste')
        Exhaust_Oil.insert(    0, 'Substrate', 'Exhaust_Oil    ')
        Sewage.insert(         0, 'Substrate', 'Sewage         ')
        Food_Ind.insert(       0, 'Substrate', 'Food_Ind       ')

        # Substrate category insertion
        Dairy_Manure.insert(   0, 'Category', 'Manure')
        Goat_Manure.insert(    0, 'Category', 'Manure')
        Chicken_Manure.insert( 0, 'Category', 'Manure')
        Sheep_Manure.insert(   0, 'Category', 'Manure')
        Pig_Manure.insert(     0, 'Category', 'Manure')
        Sow_Manure.insert(     0, 'Category', 'Manure')
        Chicken_Litter.insert( 0, 'Category', 'Manure')
        Straw.insert(          0, 'Category', 'Agricultural waste')
        Rice_Husk.insert(      0, 'Category', 'Agricultural waste')
        Sugar_Beet.insert(     0, 'Category', 'Agricultural waste')
        Dry_Grass.insert(      0, 'Category', 'Agricultural waste')
        Maize.insert(          0, 'Category', 'Agricultural waste')
        Potato_Waste.insert(   0, 'Category', 'Agricultural waste')
        Yard_Waste.insert(     0, 'Category', 'Agricultural waste')
        Bamboo.insert(         0, 'Category', 'Agricultural waste')
        Food_Waste.insert(     0, 'Category', 'Organic waste')
        Fruit_Veggie.insert(   0, 'Category', 'Organic waste')
        OFMSW.insert(          0, 'Category', 'Organic waste')
        Fish_Waste.insert(     0, 'Category', 'Organic waste')
        Slaughter_Res.insert(  0, 'Category', 'Organic waste')
        Blood.insert(          0, 'Category', 'Organic waste')
        Vinegar_Res.insert(    0, 'Category', 'Organic waste')
        Precooked_Waste.insert(0, 'Category', 'Organic waste')
        Exhaust_Oil.insert(    0, 'Category', 'Organic waste')
        Sewage.insert(         0, 'Category', 'Sludges')
        Food_Ind.insert(       0, 'Category', 'Sludges')
        print(f'database generation... [{Fore.GREEN}OK{Style.RESET_ALL}]')

    except: print(f'database generation... [{Fore.RED}DENIED{Style.RESET_ALL}]')
    try:
        PAD = pd.concat(
            [ Dairy_Manure, Goat_Manure, Chicken_Manure, Sheep_Manure, Pig_Manure, Sow_Manure, Chicken_Litter, \
            Straw, Rice_Husk, Sugar_Beet, Dry_Grass, Maize, Potato_Waste, Yard_Waste, Bamboo, Food_Waste, \
            Fruit_Veggie, OFMSW, Fish_Waste, Slaughter_Res, Blood, Vinegar_Res, Precooked_Waste, Exhaust_Oil, Sewage, Food_Ind,
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
    # save and close connection
    conn.commit()
    conn.close()

def second_averaging():
    ## ================ from PAD to SAD - secondary averaging ===============
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
    cols_all = cols
    cols = cols[2:]

    try:
        Manure_PAD    = Manure_PAD.drop(   [cols_all[0], cols_all[1]], axis=1).T.to_numpy()
        AgriWaste_PAD = AgriWaste_PAD.drop([cols_all[0], cols_all[1]], axis=1).T.to_numpy()
        OrgWaste_PAD  = OrgWaste_PAD.drop( [cols_all[0], cols_all[1]], axis=1).T.to_numpy()
        Sludges_PAD   = Sludges_PAD.drop(  [cols_all[0], cols_all[1]], axis=1).T.to_numpy()
        print(f'data extraction... [{Fore.GREEN}OK{Style.RESET_ALL}]')

    except: print(f'data extraction... [{Fore.RED}DENIED{Style.RESET_ALL}]')

    try:
        Manure_SAD    = {str(cols[i]): np.nanmean(Manure_PAD[i],    dtype='float32') for i in range (0, len(cols))}
        AgriWaste_SAD = {str(cols[i]): np.nanmean(AgriWaste_PAD[i], dtype='float32') for i in range (0, len(cols))}
        OrgWaste_SAD  = {str(cols[i]): np.nanmean(OrgWaste_PAD[i],  dtype='float32') for i in range (0, len(cols))}
        Sludges_SAD   = {str(cols[i]): np.nanmean(Sludges_PAD[i],   dtype='float32') for i in range (0, len(cols))}
        print(f'categorization... [{Fore.GREEN}OK{Style.RESET_ALL}]')

    except: print(f'categorization... [{Fore.RED}DENIED{Style.RESET_ALL}]')
    try:
        Manure     = pd.DataFrame(Manure_SAD,    index=[0])
        AgriWaste  = pd.DataFrame(AgriWaste_SAD, index=[0])
        OrgWaste   = pd.DataFrame(OrgWaste_SAD,  index=[0])
        Sludges    = pd.DataFrame(Sludges_SAD,   index=[0])

        # Substrate category insertion
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
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='SAD' ''')
        if c.fetchone()[0]==1:
            print(f'SAD table exists, upload {Fore.RED}passed{Style.RESET_ALL}')
        else:
            SAD.to_sql('SAD', conn)
            print(f'update {Fore.GREEN}successful{Style.RESET_ALL}!')
            print(f'database upload... [{Fore.GREEN}OK{Style.RESET_ALL}]')

    except: print(f'database upload... [{Fore.RED}DENIED{Style.RESET_ALL}]')

    # save and close connection
    conn.commit()
    conn.close()

def write_csv():
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

        PAD.to_csv(  PAD_path)
        SAD.to_csv(  SAD_path)
        ComDB.to_csv(ComDB_path)
        print(f'download excel file... [{Fore.GREEN}OK{Style.RESET_ALL}]')

    except: print(f'download excel file... [{Fore.RED}DENIED{Style.RESET_ALL}]')
    conn.commit()
    conn.close()

def upload_database(drop=False):
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

    # load table
    SAD   = pd.read_csv('./Database/SAD.csv')
    PAD   = pd.read_csv('./Database/PAD.csv')
    ComDB = pd.read_csv('./Database/Complete_Database.csv')

    if drop == True:
        c.execute('DROP TABLE "SAD"')
        c.execute('DROP TABLE "PAD"')
        c.execute('DROP TABLE "ComDB"')

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

    else:
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

    # save and close connection
    conn.commit()
    conn.close()