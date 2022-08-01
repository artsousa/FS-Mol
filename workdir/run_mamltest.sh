FSMOL_PATH=/home/workspace/FS-Mol
FSMOL_DATA=/home/workspace/fs_mol/data
OUTPUT_DIR=/home/workspace/output_models
MODEL_PRE=/home/workspace/output_models/FSMol_MAML_2022-07-31_09-54-53/best_validation.pkl

python $FSMOL_PATH/fs_mol/maml_test.py $FSMOL_DATA \
	--task-list-file $FSMOL_PATH/datasets/fsmol_chembl_30.json \
	--save-dir $OUTPUT_DIR --seed 10 \
	--trained-model $MODEL_PRE \
    	--train-sizes [16,32,64,128] --num-runs 3
