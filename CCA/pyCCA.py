## == Federico Moretta (c) - 2023 == ## 
import numpy as np
import pandas as pd
from datetime import date
from matplotlib import pyplot as plt
import os
from sklearn.cross_decomposition import CCA
from datetime import date
today = date.today()
from openpyxl import *
from mkdir import mkdir

def write_excel(filename, sheetname, dataframe):
    if not os.path.exists(filename):
        wb = Workbook()
        sh = wb.active
        try:
            wb.save(filename)
        except PermissionError:
            return print("Permission error occurred.")
        finally:
            print('File can be opened, please close the file before run.') 
    elif os.path.exists(filename):
        pass
    else:
        return print('Unknown error occur... please close and try again.')

    with pd.ExcelWriter(filename, engine='openpyxl', mode='a') as writer: 
        workBook = writer.book
        try:
            workBook.remove(workBook[sheetname])
        except:
            print(f"{filename} - {sheetname} - Worksheet does not exist, a new one may be added.")
        finally:
            dataframe.to_excel(writer, sheet_name=sheetname, index=False)
            writer._save()

# read data
def pyCCA():
    mkdir()
    Y = pd.read_excel(f"./{today}/{today}-output_.xlsx", sheet_name=0)
    X = pd.read_excel(f"./{today}/{today}-input_.xlsx", sheet_name=0)
    X_col = X.columns
    Y_col = Y.columns
    n_comps = min(X.shape[1], Y.shape[1])

    # compute the cca
    pyCCA = CCA(n_components=n_comps)
    pyCCA.fit(X=X, Y=Y)
    X_fit, Y_fit = pyCCA.transform(X=X, Y=Y)
    corr_coefs = [np.corrcoef(X_fit[:,i], Y_fit[:,i])[0, 1] for i in range(n_comps)]
    X_, Y_ = pyCCA.inverse_transform(X_fit, Y_fit)

    # transform everything in dataframes for output savings
    X_fit = pd.DataFrame(X_fit, columns=pyCCA.get_feature_names_out())
    Y_fit = pd.DataFrame(Y_fit, columns=Y_col)

    X_ = pd.DataFrame(X_, columns=X_col)
    Y_ = pd.DataFrame(Y_, columns=Y_col)

    coefs = pd.DataFrame(pyCCA.coef_, columns=Y_col)
    inter = pd.DataFrame(pyCCA.intercept_.reshape(1,-1), columns=Y_col)
  
    # save output
    write_excel(f"./{today}/{date.today()}-res_.xlsx", "input_fit_scaled", X_fit)
    write_excel(f"./{today}/{date.today()}-res_.xlsx", "output_fit_scaled", Y_fit)
    write_excel(f"./{today}/{date.today()}-res_.xlsx", "input_fit_inv_trans", X_)
    write_excel(f"./{today}/{date.today()}-res_.xlsx", "output_fit_inv_trans", Y_)
    write_excel(f"./{today}/{date.today()}-res_.xlsx", "input_original", X)
    write_excel(f"./{today}/{date.today()}-res_.xlsx", "output_original", Y)
    write_excel(f"./{today}/{date.today()}-res_.xlsx", "model coefficients", coefs)
    write_excel(f"./{today}/{date.today()}-res_.xlsx", "model intercepts", inter)
    
    # save figures
    comps_axes = np.linspace(1, n_comps, n_comps)
    fig, ax = plt.subplots()
    ax.plot(comps_axes, corr_coefs, 'o-k')
    ax.set_title('correlation coefficients')
    ax.set_xlabel('n_comps')
    for i, txt in enumerate(corr_coefs):
        ax.annotate("{:.2f}".format(txt), (comps_axes[i]+0.01, corr_coefs[i]+0.01))
    plt.savefig(f"./{today}/{date.today()}-corr_coeff.png")
    return print(f"ANALYSIS FINISHED, VISIT {today} FOR RESULTS.")

pyCCA()

