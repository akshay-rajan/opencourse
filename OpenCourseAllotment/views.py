import os
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.shortcuts import render, redirect
from . import allotment_algorithm
from .mongo_client import get_database


def index(request):
    """Render the home page"""
    # If not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect('/login')
    
    # Fetch the data of the current user
    coll = get_database("students")
    user = coll.find_one({"email": request.user.username})
        
    return render(request, 'OpenCourseAllotment/index.html', {
        "user": user
    })

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
        
    # Get the subjects from the database
    classes = get_database("classes")
    departments = [c["class"] for c in classes.find()]
    return render(request, "OpenCourseAllotment/register.html", {
        "departments": departments
    })

def login_view(request):
    """Enable a student or teacher to login"""
    
    if request.method == "POST":
        if request.POST["role"] == "teacher":
            id = request.POST["id"]
            password = request.POST["password"]
            user = authenticate(request, username=id, password=password)
            if user:
                login(request, user)
                return redirect('/teacher')
            else:
                return redirect('/login')
        # Get the data from the form
        email = request.POST["email"]
        password = request.POST["password"]
        # Check if the user exists
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login')
    
def apply(request):
    """Let students apply for allotment"""
    
    if not request.user.is_authenticated:
        return redirect('/login')
    
    if request.method == "POST":
        # Get the data from the form
        name = request.POST["name"]
        email = request.POST["email"]
        department = request.POST["department"]
        # Update the database
        coll = get_database("applications")
        # ToDo
        # Redirect to the home page
        return redirect('/')
    
    # Render the application form
    coll = get_database("students")
    studnet =  coll.find_one({"email": f"{request.user.username}"})
    return render(request, "OpenCourseAllotment/apply.html", {
        "student": studnet
    })