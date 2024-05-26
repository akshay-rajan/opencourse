from django.contrib.auth.models import AbstractUser
from django.db import models
from .mongo_client import get_database

class User:    
    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password
        for key, value in kwargs.items():
            if key != 'password':
                setattr(self, key, value)
            
    @staticmethod
    def get_user_by_username(username):
        db = get_database("students")
        user_data = db.find_one({'email': username})
        if user_data:
            return User(username=user_data['email'], password=user_data['password'])
        else:
            db = get_database("teachers")
            user_data = db.find_one({'teacherid': username})
            print("user_data: ", user_data)
            if user_data:
                return User(username=user_data['teacherid'], password=user_data['password'])
        return None
        
    def __str__(self):
        return self.username
