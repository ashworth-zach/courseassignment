from __future__ import unicode_literals
from django.db import models
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors["name"] = "name cannot be blank"
        if len(postData['name']) < 6 and len(postData['name']) >1:
            errors["name"] = "name must be longer than 5 characters"
        if len(postData['desc']) < 15 :
            errors["desc"] = "description cannot be less than 15 characters" 
        return errors
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of UserManager to our Course model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = CourseManager()
    # *************************
class Comment(models.Model):
    content = models.CharField(max_length=255)
    course_id=models.ForeignKey(Course, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)