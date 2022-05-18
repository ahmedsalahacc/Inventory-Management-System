#!/bin/bash
cd backend
pip install conda
conda env create -n myenv --file env.yml
conda activate myenv
cd src
python app.py