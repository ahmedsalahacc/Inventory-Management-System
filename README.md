# Inventory-Management-System

# How to download
### For the frontend
* just run `part2.sh`

### For the backend:
The needed packages can be found in `backend/env.yml` which can be installed by using miniconda, and `backend/requirements.txt` that can be operated using `virtualenv`
NOTE: Make sure that you have python 3.9.7 installed

#### Using Anaconda or Miniconda
Run The following commands:
* `cd backend`
* `conda env create -n myenv --file env.yml`
* `cd src`
* `python app.py`

Then you will find the backend operating on http://localhost:5000

#### Using virtualenv
Run the following commands
* `cd backend`
* `virtualenv venv`
* If you are running python --> run `venv/Scripts/activate.bat` else, run --> `source venv/Scripts/activate`
* `pip install -r requirements.txt`
* `cd src`
* `python app.py`

