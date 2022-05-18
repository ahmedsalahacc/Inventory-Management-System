#!/bin/bash
cd backend
pip install virtualenv
virtualenv venv
venv/Scripts/activate.bat
pip install -r requirements.txt

cd src
python app.py