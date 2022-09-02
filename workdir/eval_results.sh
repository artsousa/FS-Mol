FSMOL_PATH=/home/workspace/FS-Mol
FSMOL_DATA=/home/workspace/fs_mol/data
MODEL_PRE=/home/workspace/LOADED/FSMol_Eval_MAML_2022-08-02_02-25-59

python fs_mol/plotting/collect_eval_runs.py 'MAML' $MODEL_PRE \
    --files-suffix _eval_results --files-prefix CHEMBL \
    --metric average_precision_score
