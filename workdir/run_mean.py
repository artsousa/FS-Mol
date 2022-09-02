import os
import numpy as np
import pandas as pd

from math import nan, isnan


if __name__ == '__main__':

    frac_train = [16, 32, 64, 128]
    sumfile = ['/home/workspace/LOADED/FSMol_Eval_MAML_2022-08-02_02-25-59/summary/MAML_summary.csv']

    for sum in sumfile:
        summary = pd.read_csv(sum)
        print(sum.split('/')[-1])
        for frac in frac_train:
            values = [float(el.split('+/-')[0])
                    if type(el) is str else float('NaN') 
                    for el in summary[str(frac)+'_train'].values]

            values = [x for x in values if isnan(x) == False]

            # print(f"FRAC {frac}: ", values)
            print(f"Frac {frac} mean: {np.mean(values)}")
