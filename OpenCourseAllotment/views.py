import os
from django.conf import settings
from django.shortcuts import render, redirect
from . import allotment_algorithm
from .mongo_client import get_database


def index(request):
    """Render the home page"""
    # If not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect('/login')
    
    return render(request, 'OpenCourseAllotment/index.html')

def allotment(request):
    """Display the classes and students in each class"""
    
    file_path = os.path.join(settings.BASE_DIR, 'OpenCourseAllotment', 'file.txt')
    data = allotment_algorithm.allotStudents(file_path)
    
    return render(request, "OpenCourseAllotment/allotment.html", {
        "data": data
    })

def teacher(request):
    """Enable adding and deleting classes, and alloting students"""
    
    coll = get_database("classes")
        
    if request.method == "POST":
        clas = request.POST["class"]
        max_students = request.POST["max_students"]
        coll.insert_one({"class": clas, "max": max_students})
    
        classes = []
        for c in coll.find():
            clas = {"name": c["class"], "max_students": c["max"]}
            classes.append(clas)
        
        return render(request, "OpenCourseAllotment/teacher.html", {
            "classes": classes,
            "message": "Successfully added class!"
        })
    
    classes = []
    for c in coll.find():
        clas = {"name": c["class"], "max_students": c["max"]}
        classes.append(clas)
        
    return render(request, "OpenCourseAllotment/teacher.html", {
        "classes": classes
    })
    
def register(request):
    """Let a student register in the portal"""
    
    if request.method == "POST":
        # Get the data from the form
        username = request.POST["name"]
        dept = request.POST["department"]
        email = request.POST["email"]
        password = request.POST["password"]
        repass = request.POST["re-password"]
        # Validate password
        if password != repass:
            return render(request, "OpenCourseAllotment/register.html", {
                "message": "Passwords do not match!"
            })
        # Update the database
        coll = get_database("students")
        coll.insert_one({
            "name": username,
            "department": dept,
            "email": email, 
            "password": password
        })
        # Redirect to login page
        return redirect('/login')
        
    return render(request, "OpenCourseAllotment/register.html")