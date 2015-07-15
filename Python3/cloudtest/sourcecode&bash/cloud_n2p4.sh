#!/bin/sh
#PBS -q fast
#PBS -l nodes=edward045+edward041:ppn=4
#PBS -l walltime=01:00:00
#PBS -M zhenyal@student.unimelb.edu.au
#PBS -m abe
#PBS -N n2p4

module load openmpi-gcc
module load python/3.2.3-gcc

mpirun -np 8 python3 mpiForthTry.py $1
