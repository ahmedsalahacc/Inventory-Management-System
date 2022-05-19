#!/bin/bash
cd backend
# easy-install pip
python -m ensurepip --default-pip
pip install virtualenv

if [ -d "./venv" ] 
then
    echo "Activating VENV..."
    venv/Scripts/activate.bat
else
    echo "Creating and Activating VENV..."
    virtualenv venv
    venv/Scripts/activate.bat
fi
echo "Activated VENV"
echo "Installing necessary requirements...lal"
pip install Flask==2.1.2 Flask-Cors==3.0.10
echo "Installed all requirements"
echo "Running Flask App..."
cd src
python app.py

