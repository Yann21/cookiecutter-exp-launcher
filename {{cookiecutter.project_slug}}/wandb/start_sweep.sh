#!/usr/bin/env bash

# Start wandb and capture sweep ID
# eg. yann21/voc-scripts/hash28h1q
#GAWK='match ($0, /with: wandb agent (.*)$/, a) {print a[1]}'
SWEEP_ID=$(wandb sweep sweep.yaml 2> >(gawk 'match ($0, /with: wandb agent (.*)$/, a) {print a[1]}'))

echo Initialized run: $SWEEP_ID
echo Added ID to Dockerfile
sed -i "s@ENV WANDB_RUN=.*\$@ENV WANDB_RUN=\"$SWEEP_ID\"@" ../Dockerfile
