FSMOL_PATH=/home/workspace/FS-Mol
FSMOL_DATA=/home/workspace/fs_mol/data
OUTPUT_DIR=/home/workspace/output_models
MODEL_PRE=/home/workspace/output_models/maml_support16.pkl

python $FSMOL_PATH/fs_mol/maml_train.py $FSMOL_DATA \
    --task-list-file $FSMOL_PATH/datasets/fsmol_chembl_30.json \
    --save-dir $OUTPUT_DIR --seed 42 \
    --pretrained-model $MODEL_PRE \
    --test-metric 'avg_precision' --outer-loop-lr-scale 0.1 --max-epochs 50 \
    --patience 25 --task-batch-size 16 --train-size 16 --test-size 128 \
    --min-test-size 32 --max-num-inner-train-steps 6 \
    --metatrain-task-specific-parameters True --validation-train-set-sizes [8,16,32] \
    --validation-test-set-size 256 --validation-num-samples 5
