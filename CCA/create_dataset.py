## == Federico Moretta (c) - 2023 == ## 
import pandas as pd
import numpy as np
import os
from mkdir import mkdir

def createDataset(excelFileName, sheet_name=0):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',\
                'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    mkdir()
    # read raw dataset from excel file
    raw_ds = pd.read_excel(excelFileName, sheet_name=sheet_name, index_col=0)
    col_name = raw_ds.columns

    # read input/output excel code
    if not os.path.exists("input_output_split.xlsx"):
        from openpyxl import Workbook
        ios_file = "input_output_split.xlsx"
        wb = Workbook()
        sh = wb.active
        for i in range(len(col_name)):
            sh[f'{alphabet[i]}1'] = col_name[i]
            sh[f'{alphabet[i]}2'] = 0
            try:
                wb.save(ios_file)
            except PermissionError:
                wb.save(ios_file)
                wb.close()
                return print("Permission error occurred")
        return print('File can be opened, please close the file before run.') 
    elif os.path.exists("input_output_split.xlsx"):
        input_output_split = pd.read_excel("input_output_split.xlsx")
    else:
        return print('Unknown error occur... please close and try again.')

    # select and write only input columns (excluding rows with zero vals)
    input_dict = {}; output_dict = {}
    split_array = input_output_split.iloc[0].to_list()
    for i in range(len(split_array)):
        indx = split_array[i]
        if indx == 0:
            pass
        elif indx == 1:
            selected_col_name = col_name[i]
            selected_col_vals = raw_ds[selected_col_name].to_list()
            input_dict.update({selected_col_name: selected_col_vals})
        elif indx == 2:
            selected_col_name = col_name[i]
            selected_col_vals = raw_ds[selected_col_name].to_list()
            output_dict.update({selected_col_name: selected_col_vals})       
            
    input_df = pd.DataFrame(input_dict)
    output_df = pd.DataFrame(output_dict)
    
    # dropping rows with empty cells
    input_df.dropna(axis=0, how='any', inplace=True)
    output_df.dropna(axis=0, how='any', inplace=True)

    # upload values to excels
    from datetime import date
    today = date.today()
    input_df.to_excel(f'./{today}/{today}-input_.xlsx', index=False)
    output_df.to_excel(f'./{today}/{today}-output_.xlsx', index=False)