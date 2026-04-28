# 🚀 FastAPI User Registration System

A full-stack user registration system built using FastAPI and PostgreSQL with secure password handling and validation.


## 🛠️ Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Jinja2 Templates
- HTML & CSS
- bcrypt (Password Hashing)


## ✨ Features

- User registration form
- Password hashing using bcrypt
- Input validation (empty fields, password length, mismatch)
- Template-based error handling
- Success page after registration
- Static CSS integration
- Clean project structure


## 📁 Project Structure

Registration_App/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
│
├── templates/
│   ├── form.html
│   ├── success.html
│   ├── error_email_exists.html
│   ├── error_empty_message.html
│   └── error_password_message.html
│
└── static/
    └── css/
        ├── form.css
        ├── success.css
        ├── error_email_exists.css
        ├── error_empty_message.css
        └── error_password_message.css



## ⚙️ How to Run

1. Install dependencies:
pip install fastapi uvicorn sqlalchemy psycopg2 passlib bcrypt jinja2

2. Run the server:
uvicorn main:app --reload

3. Open in browser:
http://127.0.0.1:8000/


## 🌐 Live Demo

https://fastapi-registration-system.onrender.com

## 🔐 Validation Logic

- Prevents empty input fields
- Ensures password length ≥ 6 characters
- Confirms password match
- Trims unnecessary spaces before processing


## 🎯 Purpose

This project demonstrates backend development skills including API handling, database integration, validation logic, and secure authentication practices.


## 👤 Author
White | GitHub: CodeDaniel23