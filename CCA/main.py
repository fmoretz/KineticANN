import numpy as np
import pandas as pd
from time import ctime 
import matplotlib.pyplot as plt
from create_dataset import createDataset as cd
from pyCCA import pyCCA
import warnings
warnings.filterwarnings("ignore")

def main():
    cd("./results_from_CCA.xlsx", sheet_name="db_v2")
    pyCCA()
    return print(f"Finished - {ctime()}")

if __name__ == "__main__":
    main()
