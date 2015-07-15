#!/bin/sh
#PBS -q fast
#PBS -l nodes=edward028:ppn=8
#PBS -l walltime=01:00:00
#PBS -M zhenyal@student.unimelb.edu.au
#PBS -m abe
#PBS -N n1p8

module load openmpi-gcc
module load python/3.2.3-gcc

mpirun -np 8 python3 mpiTry.py $1
