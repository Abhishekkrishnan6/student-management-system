A student management system built using Django framework. It is designed for interactions between students and teachers. Features include attendance, marks and time table.


## Installation

Python and Django need to be installed

```bash
pip install django
```

## Usage

Go to the student-management-system folder and run

```bash
python manage.py runserver
```
Then go to the browser and enter the url **http://127.0.0.1:8000/**


## Login

The login page is common for Admin ,Staff and Student.

You can access the django admin page at **http://127.0.0.1:8000/admin**

like email = abhii@gmail.com
password = 1234567890

Also a new admin user can be created using

```bash
python manage.py createsuperuser
```

## Users

New students and teachers can be added through the admin page. A new user needs to be created for each.
The admin page is used to modify all tables such as Students, Teachers, Departments, Courses, Classes etc.
