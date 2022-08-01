FSMOL_PATH=/home/workspace/FS-Mol
FSMOL_DATA=/home/workspace/fs_mol/data
OUTPUT_DIR=/home/workspace/output_models/summary
MODEL_PRE=/home/workspace/output_models/FSMol_Eval_MAML_2022-08-01_09-04-39

python fs_mol/plotting/collect_eval_runs.py 'MAML' $MODEL_PRE \
    --files-suffix _eval_results --files-prefix CHEMBL \
    --metric average_precision_score
