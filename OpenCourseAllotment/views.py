import os
from django.conf import settings
from django.shortcuts import render
from . import allotment_algorithm
from .mongo_client import get_database


def index(request):
    """Render the home page"""
    
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
    classes = []
    for c in coll.find():
        clas = {"name": c["class"], "max_students": c["max"]}
        classes.append(clas)
    
    return render(request, "OpenCourseAllotment/teacher.html", {
        "classes": classes
    })
    
