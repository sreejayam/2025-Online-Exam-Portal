# Online Exam System (Django)

## Overview
This project is a simple Online Examination System built using Django as part of a backend developer assessment.

## Features

### User
- Login authentication
- View subjects and available exams
- Attempt exams with time limit
- Automatic exam submission after time expiry
- View exam result with unique Result ID
- Search exam result using Result ID

### Admin
- Create subjects
- Create exams under subjects
- Define exam duration and availability dates
- Add multiple questions per exam
- Control number of questions shown to users

## Tech Stack
- Python
- Django
- SQLite
- HTML, JavaScript

## Exam Timing
- Exam duration is handled using a frontend JavaScript countdown timer.
- Exam auto-submits once time expires.

## How to Run
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
