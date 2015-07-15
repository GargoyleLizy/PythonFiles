#!/bin/sh
#PBS -q parallel
#PBS -l nodes=2:ppn=4
#PBS -l walltime=00:05:00
#PBS -M zhenyal@student.unimelb.edu.au
#PBS -m abe
#PBS -N test_n2p8

module load openmpi-gcc
module load python/3.2.3-gcc

mpirun -np 8 python3 test_n1p8.py $1
