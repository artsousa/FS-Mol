import os
import pandas as pd

molfile = '/tmp/fs_mol/cleaned/CHEMBL973406.csv'

df = pd.read_csv(molfile)
print(df.head(33))
print(df.info())
