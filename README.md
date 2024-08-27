# Open Course Allotment System

An interface for students to register and choose their courses, and for admins to allot students based on their choices and academic performance.


![alt text](./OpenCourseAllotment/static/OpenCourseAllotment/ER.png)

## Flow

[Views](./OpenCourseAllotment/views.py) | [Models](./OpenCourseAllotment/models.py) | [Urls](./OpenCourseAllotment/urls.py) | [Templates](./OpenCourseAllotment/templates/OpenCourseAllotment/) | [Styles](./OpenCourseAllotment/static/OpenCourseAllotment/)
---|---|---|---|---

#### Student
1. Registers through [register.html](./OpenCourseAllotment/templates/OpenCourseAllotment/register.html).
2. Logs in through [login.html](./OpenCourseAllotment/templates/OpenCourseAllotment/login.html).
3. After logging in, the student is taken to [Home Page](./OpenCourseAllotment/templates/OpenCourseAllotment/index.html), where the details about the student, courses and allotment are displayed.
4. Applies for allotment: [apply.html](./OpenCourseAllotment/templates/OpenCourseAllotment/apply.html).

#### Teacher

1. Logs in through [login.html](./OpenCourseAllotment/templates/OpenCourseAllotment/login.html) using given credentials.
2. Taken to [Home](./OpenCourseAllotment/templates/OpenCourseAllotment/index.html), where the details about the applications and the status of classes are displayed.
3. If `Allot` is triggered, the students are alloted and the teacher is taken to a page displaying the status of the classes.

## Usage

Clone the project:
```bash
git clone https://github.com/akshay-rajan/opencourse.git
```
Create and activate the virtual environment:
```bash
# Windows
py -m venv venv
.\venv\Scripts\activate
```
Install MongoDB. 
Then install the requirements:
```bash
pip install -r requirements.txt
```
Run the Django server:
```bash
python manage.py runserver
```
The application is now live at http://127.0.0.1:8000/.

