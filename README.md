# To Do List
Django project where you can manage your tasks.

## Overview
This project is a simple yet powerful task management application built with Django. It allows users to create, update, delete, and manage tasks and tags. The main features and technologies used in this project are highlighted below.

## Features
- **Task Management:** Create, read, update, and delete tasks.
- **Tag Management:** Add tags to tasks and manage them separately.
- **User Authentication:** Secure user authentication to manage personal tasks.
- **Responsive Design:** The user interface is designed to be responsive and user-friendly.

## Technologies Used
- Django
- Python 3
- HTML5
- CSS3
- Bootstrap5

## Installation
Ensure Python 3 is already installed on your system. Follow these steps to set up the project locally:

1. **Clone the repository:**
```bash
https://github.com/oleksandra-shershen/to-do-list.git
cd to-do-list
```
This command downloads the project files to your local machine and changes your current directory to the project's root.

2. **Switch to the development branch:**
```bash
git checkout -b develop
```
This command creates and checks out a new branch called 'develop', which is typically used for development purposes.

3. **Set up a Python virtual environment:**
```bash
python3 -m venv venv
```

4. **Activate the virtual environment:**
- On macOS/Linux:
```bash
source venv/bin/activate
```
- On Windows:
```bash
venv\Scripts\activate
```
Creating a virtual environment isolates your Python/Django setup on a per-project basis, ensuring that dependencies from different projects do not conflict.

5. **Install the required packages:**
```bash
pip install -r requirements.txt
```

6. **Run database migrations:**
```bash
python manage.py migrate
```
This command applies database migrations to your DBMS. It's essential for setting up or updating your database schema.

7. **Start the Django development server:**
```bash
python manage.py runserver
```
Launches the Django development server, allowing you to access the web application via http://127.0.0.1:8000/ in your web browser.

## Demo