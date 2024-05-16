from django.shortcuts import render


def index(request):
    """Render the home page"""
    
    return render(request, 'OpenCourseAllocationPortal/index.html')

def allotment(request):
    """Display the classes and students in each class"""
    
    data = {}
    
    return render(request, "OpenCourseAllocationPortal/allotment.html", {
        "data": data
    })

