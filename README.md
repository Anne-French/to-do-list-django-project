# to-do-list-django-project

This is a web application for managing a to-do list. The backend is built with Django and Django Rest Framework, while the frontend is developed using Vue.js. This README provides instructions on setting up and running the application.
Project Structure

    Backend: Django and Django Rest Framework
    Frontend: Vue.js

Prerequisites

    Python 3.8 or higher
    Node.js 14.x or higher
1.Clone the Repository
git clone https://github.com/Anne-French/to-do-list-django-project
cd todo-project/backend

2.Create a Virtual Environment
python -m venv venv

3.Activate the Virtual Environment
venv\Scripts\activate

4. Install Dependencies
pip install asgiref==3.8.1
Django==5.0.7
django-cors-headers==4.4.0
djangorestframework==3.15.2
sqlparse==0.5.1
tzdata==2024.1

5.Apply Migrations
python manage.py migrate

6.Run the Development Server
python manage.py runserver

The backend will be accessible at http://localhost:8000.

Frontend Setup

Navigate to the Frontend Directory
cd ../frontend

Install Dependencies
npm install

Run the Development Server
npm run serve

Once both the backend and frontend servers are running, you can interact with the application through the Vue.js interface. You can add, edit, and delete to-do items, which will be managed by the Django REST API.

To run tests for the backend:
python manage.py test

For frontend tests, you can use:
npm run test


