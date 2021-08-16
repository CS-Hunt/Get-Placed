#
<div align="center">
<img src="https://github.com/CS-Hunt/Get-Placed/blob/master/app/static/app/images/logo.jpeg" width="20%">
<b>
</b>
<h1>Welcome to the Get Placed Repository</h1>

<a href="https://t.me/joinchat/YKR5_lOCNppiZjNl">![Telegram Community](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)</a>
<a href="mailto:info.cshunt@gmail.com">![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a>
<a href="https://open.vscode.dev/CS-Hunt/Get-Placed.git"><img src="https://open.vscode.dev/badges/open-in-vscode.svg" height="25px"></a>

</div>

<br/>

## Getting Started

If you are trying to use this project for the first time, you can get up and running by following these steps.

To contribute to this project, please see the [contributing guidelines](https://github.com/CS-Hunt/Get-Placed/blob/master/Contributing.md).


## Install and Run

Make sure you have **Python 3.x** installed and **the latest version of pip** *installed* before running these steps.

Clone the repository using the following command

```bash
git clone git@github.com:CS-Hunt/Get-Placed.git
# After cloning, move into the directory having the project files using the change directory command
cd Get-Placed
```
Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python -m venv env
```
Activate the virtual environment

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```
Install all the project Requirements
```bash
pip install -r requirements.txt
```
-Apply migrations and create your superuser (follow the prompts)

```bash
# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser
```

Run the development server

```bash
# run django development server
python manage.py runserver
```
## Reviewers

After submitting your PR, please tag reviewer(s) in your PR message. You can tag anyone below for the following.

<br/>

- **Markdown, Documentation, Email templates:**

  [@Nitesh - Nitesh-Singh-5](https://github.com/Nitesh-Singh-5)

#

- **Frontend, API, Backend, Databases, Dependencies:**

     --> *Choose two reviewers :*

    [@Nitesh - Nitesh-Singh-5](https://github.com/Nitesh-Singh-5)


## Explore admin panel for model data or instances

http://127.0.0.1:8000/admin or http://localhost:8000/admin

## Login with the user credentials (you created) using "createsuperuser" cmd

> ⚠ If everything is good and has been done successfully, your **project** should be hosted on port 8000 i.e http://localhost:8000/

