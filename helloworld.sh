#!/bin/bash
#SBATCH --job-name=helloworld            # Job name
#SBATCH --output=.out/result_%j.out      # Standard output file (%j expands to jobId)
#SBATCH --error=.out/result_%j.err       # Standard error file
#SBATCH --ntasks=1                       # Number of tasks
#SBATCH --cpus-per-task=1                # Number of CPU cores per task
#SBATCH --mem=2GB                        # Memory per node
#SBATCH --time=0-00:05:00                # Time limit days-hrs:min:sec
#SBATCH --mail-type=ALL --mail-user=sharvey@flatironinstitute.org


module load python
srun hostname
srun python train_simple_network.py