#!/bin/bash
echo 'p4' | sudo -S make clean
rm /home/p4/Planter/src/targets/bmv2/software/model_test/test_environment/*.p4
cp /home/p4/Planter/P4/RF_performance_Iris.p4 /home/p4/Planter/src/targets/bmv2/software/model_test/test_environment/RF_performance_Iris.p4
echo 'h1 python3 /home/p4/Planter/src/test/test_switch_model_bmv2_software.py' | sudo -S make run
