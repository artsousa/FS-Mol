#!/bin/bash

FSMOL_DATA=/tmp/fs_mol/data
FSMOL_PATH=/home/arthurvitoria/workspace/FS-Mol
OUTPUT_DIR=/tmp/outputs
MODEL=kNN

python fs_mol/baseline_test.py $FSMOL_DATA \
	--task-list-file $FSMOL_PATH/datasets/fsmol_chembl_30.json \
	--save-dir $OUTPUT_DIR_$MODEL/evaluation --num-runs 3 --seed 10 \
	--model $MODEL \
	--train-sizes [16,32,64,128] --grid-search True
