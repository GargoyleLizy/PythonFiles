#!/bin/sh
#PBS -q serial
#PBS -l nodes=1:ppn=1
#PBS -l walltime=12:00:00
#PBS -M zhenyal@student.unimelb.edu.au
#PBS -m abe
#PBS -N mut_n1p1

module load openmpi-gcc
module load python/3.2.3-gcc

mpirun -np 1 python3 mpiForthTry.py $1 
