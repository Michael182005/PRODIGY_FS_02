# Django Employee Management System

This is a Django-based Employee Management System with staff user authentication and CRUD operations for employees.

## Features

- Staff user login/logout using Django's built-in authentication
- Employee CRUD (Create, Read, Update, Delete) with validations:
  - Unique email
  - Phone number regex validation
  - Positive salary
- Responsive UI with Bootstrap 5
- Security features: CSRF protection, session management
- User-friendly templates with base layout and navigation
- Automated tests for models, views, and forms

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository or copy the project files.

2. Navigate to the project directory:

```bash
cd employee_management_django
```

3. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Apply migrations:

```bash
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver 8001
```

8. Open your browser and go to:

```
http://127.0.0.1:8001/
```

9. Log in with your superuser credentials.

## Usage

- After login, you can view the list of employees.
- Add, update, or delete employees using the provided UI.
- Logout using the link in the navigation bar.

## Notes

- Place a valid `favicon.ico` file in the `static` directory (`employee_management_django/static/favicon.ico`) to avoid 404 errors for the favicon.
- The logout view supports both GET and POST requests to avoid HTTP 405 errors.

## License

This project is open source and free to use.
