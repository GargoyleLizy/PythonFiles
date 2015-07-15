#!/bin/sh
#PBS -q fast
#PBS -l nodes=1:ppn=8
#PBS -l walltime=00:30:00
#PBS -M zhenyal@student.unimelb.edu.au
#PBS -m abe

module load openmpi-gcc
module load python/3.2.3-gcc

mpirun -np 8 python3 mpiTry.py $1