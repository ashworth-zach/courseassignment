from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course
def index(request):
    context={
        'courses':Course.objects.all().values()
    }
    return render(request, 'courseapp/index.html', context)
def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/courses')
    else:
        courses = Course.objects.create()
        courses.name = request.POST['name']
        courses.desc = request.POST['desc']
        courses.save()
        return redirect('/courses')
def destroy(request, course_id):
    course = Course.objects.get(id =course_id)
    context={
        'course':course
    }
    return render(request,'courseapp/delete.html',context)
def deletecourse(request, course_id):
    course = Course.objects.get(id =course_id)
    course.delete()
    return redirect('/courses')