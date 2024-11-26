# Role-Based Access Control (RBAC) with Django and Simple JWT

## Overview

This project demonstrates a secure Role-Based Access Control (RBAC) system using Django and Simple JWT. It includes:

- User Authentication and Role Management
- Role-Based Permissions
- Secure Authentication with JWT Tokens
- Endpoints for managing roles, users, and protected resources

---

## Features

- Authentication: Secure registration, login, and logout functionality with JWT.
- Authorization: Role-based authorization system with custom permissions.
- Roles: Admin, Moderator, and User roles, each with specific permissions.
- Token Blacklisting: Secure logout with token invalidation.

---

## Installation

### 1. Clone the Repository
git clone https://github.com/Uvesh8085/RBAC.git/
cd <project-directory>

Step 2: Create and Activate a Virtual Environment

Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Step 3: Install Dependencies
Install the required Python packages:


Copy code
pip install -r requirements.txt
Step 4: Run Migrations
Apply database migrations:


Copy code
python manage.py makemigrations
python manage.py migrate
Step 5: Create a Superuser
Create a superuser to access the admin panel:


Copy code
python manage.py createsuperuser
Step 6: Run the Development Server
Start the Django development server:


Copy code
python manage.py runserver
Access the API at http://127.0.0.1:8000.

API Endpoints
Authentication
Register: POST /api/users/register/
Login: POST /api/token/
Logout: POST /api/logout/
Role Management
Create Role: POST /api/users/roles/
List Roles: GET /api/users/roles/
User Management
Get User Details: GET /api/users/
Edit User: PUT /api/users/<id>/
Testing the API
Use tools like Postman to test the API endpoints. Ensure to include the JWT token in the Authorization header for endpoints requiring authentication.

json
Copy code
Authorization: Bearer <access_token>
Troubleshooting
Ensure the virtual environment is activated before running the server or installing dependencies.
Use the Django admin panel (http://127.0.0.1:8000/admin) to manage roles and permissions.
Contributing
Feel free to fork the repository and create pull requests. Any suggestions or issues can be reported in the issue tracker.

License
This project is licensed under the MIT License.

yaml
Copy code

---

### Steps to Push the Project to GitHub

1. Initialize a Git Repository:
   Navigate to your project directory and initialize Git.

   ```
   git init
Create a .gitignore File: Add a .gitignore file to exclude unnecessary files. Example:


Copy code
venv/
*.pyc
__pycache__/
db.sqlite3
.env
