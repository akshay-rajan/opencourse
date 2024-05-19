from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("allotment", views.allotment, name="allotment"),
    path("teacher", views.teacher, name="teacher"),
    path('login/', auth_views.LoginView.as_view(template_name='OpenCourseAllotment/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='OpenCourseAllotment/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
