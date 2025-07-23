TEXTRON-BACK
Backend for the TEXTRON project, a full-stack application demonstrating Python skills with FastAPI, JWT authentication, and MySQL.
Features

REST API: Built with FastAPI for high-performance endpoints.
User Authentication: Secure registration and login using JWT.
Database: MySQL for storing user data with SQLAlchemy ORM.

Setup

Clone the repository:git clone https://github.com/your-username/textron-back.git


Create a virtual environment and install dependencies:python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


Set up MySQL and create a textron database:CREATE DATABASE textron;


Update main.py with your MySQL credentials.
Run the API:uvicorn main:app --reload



Endpoints

POST /register: Create a new user.
POST /login: Authenticate and receive a JWT.
GET /users/me: Retrieve authenticated user details (requires JWT).

Technologies

Python, FastAPI, SQLAlchemy, PyMySQL
JWT (python-jose)
Password hashing (passlib with bcrypt)
Form data parsing (python-multipart)

License
MIT License
