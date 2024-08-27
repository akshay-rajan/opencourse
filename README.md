# Open Course Allotment System

An interface for students to register and choose their courses, and for admins to allot students based on their choices and academic performance.


![alt text](./OpenCourseAllotment/static/OpenCourseAllotment/ER.png)


* [Views](./OpenCourseAllotment/views.py)
* [Models](./OpenCourseAllotment/models.py)
* [Urls](./OpenCourseAllotment/urls.py)
* [Templates](./OpenCourseAllotment/templates/OpenCourseAllotment/)
* [Styles](./OpenCourseAllotment/static/OpenCourseAllotment/)

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

