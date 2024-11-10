# About the project
This is a full stack hospital management website where patients can register and login to their account to see information on different departments and their doctors .This also helps to schedule their appointments to see a specific doctor on your available date.
The appointment details will be saved in the database. The staff or authorized person will be able to recieve the details of appointment in their admin panel which requires authorization. The confirmation will be sent once the appointment will be scheduled.
## Built with
* Frontend - HTML, CSS, JavaScript, Bootstrap
* Backend - Python
* Framework - Django
* Database - SQLite
## Getting Started
### 1. Install Python
Ensure Python is installed on your system. You can check this by running:
python --version

If Python is not installed, download and install it from the official Python website.

### 2. Install pip
Ensure pip (Python package installer) is installed by running:
pip --version
or:

pip3 --version
If not installed, you can install pip by following the instructions here.

### 3. Install Django
Install Django using pip:

pip install django

### 4. Verify Installation
To verify that Django is installed, run:

bash
Copy code
python -m django --version

python3 -m django --version

### 5. Start a Django Project
You can start a new Django project by running:

django-admin startproject projectname
Replace projectname with the desired name of your project.

Optional: Virtual Environment (Recommended)
It's a good practice to use a virtual environment to manage dependencies for your project:

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install django
