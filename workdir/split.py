import os
import json
import pprint
import random
import shutil
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split


if __name__ == '__main__':

    seed = 10
    random.seed(seed)
    np.random.seed(seed)

    df = pd.read_csv('/tmp/fs_mol/cleaned/summary.csv')
    ptasks = os.listdir('/tmp/fs_mol/processed')
    ptasks = [el.split('.')[0] for el in ptasks]
    
    print(f"processed tasks {len(ptasks)}")
    print(f"We have {df.cleaned_size.sum()} measurements from our first pass of cleaning (cleaning_failed == False)")

    df = pd.concat(
            [
                df.loc[df['target_id'].notna()].astype({"target_id": int}).astype({"target_id": str}),
                df.loc[df['target_id'].isna()]
            ],
            ignore_index=True
    )

    # select only tasks that were processed
    df = df[df.chembl_id.isin(ptasks)]
    print(f"Total rows id {len(df.chembl_id)}")
    
    df = df[df.cleaned_size>=32] # Select out very small assays 
    df = df[df.cleaned_size<=5000]

    print(f"Total rows id after cleaning: {len(df.chembl_id)}")
    print(f"We have {len(df[df.target_id.notna()].target_id.unique())} unique known targets")
    print(f"Total targets id {len(df[df.target_id.notna()].target_id)}")

    print(''.join(['-'] * 128))
    print('Select best tasks for test...')

    possible_test = df[df.target_id.notna()]

    best = possible_test.loc[
        (possible_test["cleaned_size"] >= 128) &
        (possible_test["confidence_score"] >= 8) &
        (possible_test["percentage_pos"] <= 70) &
        (possible_test["percentage_pos"] >= 30) &
        (possible_test["cleaned_size"] <= 5000)
    ]

    best.reset_index(inplace=True)

    print(f"We have {len(set(best.target_id.unique()))} possible test targets")

    id_test, id_val = train_test_split(best.target_id.unique(), test_size=0.5, shuffle=True, random_state=seed)
    
    id_val = id_val[:50]
    id_test = id_test[:250]

    def get_tasks(ids, dataset, into=True):
        df_ids = set()
        for i in range(len(ids)):
            ids2 = set(dataset[dataset.target_id == ids[i]].target_id.head(1).index) # Get rows where target_id == ids[i]
            df_ids = df_ids.union(ids2)

        return df_ids

    id_test = get_tasks(id_test, best)
    test_set = best.iloc[list(id_test)]
    print(test_set.head())
    
    id_val = get_tasks(id_val, best)
    val_set = best.iloc[list(id_val)]
    print(val_set.head())

    train_set = possible_test.loc[
         (~possible_test['chembl_id'].isin(best.chembl_id))
    ]
    print(train_set.head())

    datasetj = {
            'train': list(train_set.chembl_id.values), 
            'valid': list(val_set.chembl_id.values),
            'test': list(test_set.chembl_id.values)}
    
    dest_path = '/tmp/fs_mol/data'
    orig_path = '/tmp/fs_mol/processed'
  
    with open('/home/arthurvitoria/workspace/FS-Mol/datasets/fsmol_chembl_30.json', 'w') as f:
        json.dump(datasetj, f)
        f.close()

    for key in list(datasetj.keys()):
        fpath = os.path.join(dest_path, key)
        if os.path.isdir(fpath):
            shutil.rmtree(fpath)
        os.makedirs(fpath, exist_ok=True)
    
        for cid in datasetj[key]:
            jsonn = cid + '.jsonl.gz'
            taskname = os.path.join(orig_path, jsonn)
            
            shutil.copyfile(
                    taskname,
                    os.path.join(taskname, os.path.join(fpath, jsonn))
            )






     
