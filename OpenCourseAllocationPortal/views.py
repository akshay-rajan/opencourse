from django.shortcuts import render

def index(request):
    """Render the home page"""
    
    return render(request, 'OpenCourseAllocationPortal/index.html')
