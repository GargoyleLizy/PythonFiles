#!/bin/sh
#PBS -q serial
#PBS -l nodes=1:ppn=1
#PBS -l walltime=00:10:00
#PBS -M zhenyal@student.unimelb.edu.au
#PBS -m abe
#PBS -N test_n1p1

module load openmpi-gcc
module load python/3.2.3-gcc

python3 test_n1p1.py $1 $2
