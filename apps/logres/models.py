from __future__ import unicode_literals
from django.db import models
import re, bcrypt

# Create your models here.
class UserManager(models.Manager):
    def register(self, postData):
        # store the possible failed validations
        errors = []
        # first_name length greater than 2
        if len(postData['name']) < 3:
            errors.append('Name must be at least 3 characters long!')
        # last_name length greater than 2
        if len(postData['username']) < 3:
            errors.append('Username must be at least 3 characters long!')
        if postData['date'] == '':
            errors.append('Please enter hire date')
            print postData['date']
        # password must be at least 8
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters!')
        #passwords must match
        if not postData['password'] == postData['confirm_password']:
            errors.append('Passwords must match!')

        user = self.filter(username = postData['username'])
        # email must be unique
        if user:
            errors.append('Username must be unique')

        modelResponse = {}
        # if failed validations
        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        else:
            hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = self.create(name = postData['name'], username = postData['username'], hire_date = postData['date'], password = hashed_password)
            modelResponse['status'] = True
            modelResponse['user'] = user
        return modelResponse

    def login(self, postData):
        # check to see if user is in DB
        user = self.filter(username = postData['username'])
        modelResponse = {}
        print user
        # if user exsits
        if user:
            # check for matching passwords
            if bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                # send success to views
                modelResponse['status'] = True
                modelResponse['user'] = user[0]
            # fail match password
            else:
                # send error message to views
                modelResponse['status'] = False
                modelResponse['errors'] = 'Invalid Username/password combination'
        else:
            modelResponse['status'] = False
            modelResponse['errors'] = 'Invalid Username'

        return modelResponse

class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.TextField(max_length=100)
    hire_date = models.DateField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
