Mini Task Management System
A simple web-based task management system to perform CRUD operations (Create, Read, Update, Delete) on tasks.

Features
-Add tasks with a name, description, and due date.
-View all tasks in a list.
-Update task status (mark as completed or pending).
-Delete tasks.


Technologies Used

-Backend: Django (Python)
-Database: MySQL
-API Testing: Postman

   Setup Instructions

1. Clone the Repository

git clone https://github.com/dalvenjose/Task_Management_System.git

2. Install Dependencies

pip install -r requirements.txt

3. Configure the Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<db_name>',
        'USER': '<username>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
-Create the database schema

 python manage.py makemigrations
 python manage.py migrate

4. Run the Development Server

python manage.py runserver



Postman Collection

You can find the exported Postman collection in the Postman/ folder. Import it into Postman to test the API endpoints.


