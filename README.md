# Job Application Tracker

A Django web app to track job applications.

## Features
- User signup, login, and logout
- Add, edit, delete, and search applications
- Dashboard with status counts and a Chart.js chart
- Each user sees only their own data

## Tech Stack
Python, Django, SQLite, Bootstrap 5, Chart.js

## Setup
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver