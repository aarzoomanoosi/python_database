
# python_database

Sample code to connect with Sqlite Database to use
- Data Api
- ORM

## Setup the local python environment

The following url can be used and find python software to install

#### Download website: `https://www.python.org/downloads/`

## Setup a git repo locally
- Create a project folder `python_database`
- Go to the project folder
- Clone the code
	- c:\> `git clone <git repo url>`  [Hit Enter Key]	
- Go to the project directory
	- c:\> `cd python_database`
	- c:\python_database>
- Setup a feature branch
	- c:\python_database> `git checkout -b <feature_branch_name>`   [Hit Enter Key]

## Setup a virtual environemnt
- Run following command to install a virtual environment module from pip
	- c:\python_database> `pip install virtualenv`   [Hit Enter Key]
- Run the following command to **create a virtual environment**
	- c:\python_database> `python -m venv venv`   [Hit Enter Key]
- **Activate** virtual environment
	- c:\python_database> `env/Scripts/activate.bat` //In CMD
	- c:\python_database> `env/Scripts/Activate.ps1` //In Powershel
	- c:\python_database> `env/Scripts/activate.bat`
	- (venv) c:\python_database>
- **Deactivate** your virtual environment, simply run the following code in the terminal:
	- (venv) c:\python_database> `deactivate`   [Hit Enter Key]

## Install all dependencies locally
- Run the following command to **install all required libraries** at once, first go to virtual environment per above steps
- > (venv) c:\python_database> `pip install -r requirements.txt`  [Hit Enter Key]

## When code is ready to push
- Freeze the development or Generate project's dependencies file
	- (venv) c:\python_database> `pip freeze > requirements.txt`   [Hit Enter Key]

## Run the code
- (venv) c:\python_database> `pip app-data.py`