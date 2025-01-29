# HNG Stage 0 Task - GitHub Repository
# Project Description
This project is part of the HNG Internship Stage 0 Task. It is designed to demonstrate essential skills in backend development, particularly in Python and Django. The project includes an API that returns user information (email, current date and time, and GitHub URL) in a JSON format. The project serves as a basic example of handling API requests and JSON responses in Django.

# Setup Instructions
# Prerequisites
Before running this project, make sure you have the following installed:

Python 3.8+
Django 3.2+
Django REST framework

# Installation 
1 Clone this repository to your local machine:

git clone https://github.com/RexDavid06/HNG-stage-0Task.git
cd HNG-stage-0Task

2 Create a virtual environment:
python3 -m venv venv
source venv/bin/activate # For Linux/Mac
venv\Scripts\activate # For Windows

3 Install the required dependencies:
pip install -r requirements.txt

4 Run database migrations:
python manage.py migrate

5 Start the development server:
python manage.py runserver

# API Documentation
Endpoint URL
The API exposes a single endpoint:

GET /home/

Request:
This endpoint doesn't require any parameters or body in the request.

Response:
The API returns a JSON object containing:

{
    "data": [
        {
            "email": "user@example.com",
            "current_datetime": "YYYY-MM-DDTHH:MM:SS.ssssssZ",
            "github_url": "https://github.com/YourGitHubUsername/HNG-stage-0Task"
        }
    ]
}

# Example Usage
Request:

curl -X GET http://localhost:8000/api/home/

# Response:
{
    "data": [
        {
            "email": "rhexmilia06@gmail.com",
            "current_datetime": "2025-01-29T12:50:28.081757Z",
            "github_url": "https://github.com/RexDavid06/HNG-stage-0Task"
        }
    ]
}

# Backlink
For more information about hiring Python developers, visit:
Hire Python Develope