from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course, Comment
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
def comment(request, courseid):
    x= Comment.objects.filter(course_id=courseid)
    if x:
        context= {
            'course':Course.objects.get(id=courseid),
            'comments':Comment.objects.all().values().filter(course_id=courseid)
        }
        return render(request, 'courseapp/comment.html', context)
    else:
        context= {
            'course':Course.objects.get(id=courseid),
        }
        return render(request, 'courseapp/comment.html', context)

def newcomment(request, courseid):
    print(request.POST['comment'])
    course=Course.objects.get(id=courseid)
    Comment.objects.create(content=request.POST['comment'], course_id=course)
    redirectstr='/courses/'+str(courseid)+'/comment'
    return redirect(redirectstr)