#!/bin/bash

loop_count=50

for i in $(seq 1 $loop_count)
do
   echo "这是第 $i 次迭代"
   python TEST_CS_ISTA_Net.py --layer_num 5 --cs_ratio 25 --learning_rate 1e-4 --loss_weight 0.01  --noise_mode 'cs' --epoch_num 1200
done


for i in $(seq 1 $loop_count)
do
   echo "这是第 $i 次迭代"
   python TEST_CS_ISTA_Net.py --layer_num 5 --cs_ratio 25 --learning_rate 1e-4 --loss_weight 2  --noise_mode 'pcs' --epoch_num 1200
done

#for i in $(seq 100 100 1200)
#do
#   python TEST_CS_ISTA_Net.py --layer_num 5 --cs_ratio 25 --learning_rate 1e-4 --loss_weight 2  --noise_mode 'pcs' --epoch_num $i | tee -a test_output.txt
#done

