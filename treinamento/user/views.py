from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher, Student


def teacher_list(request):
    teacher_list = Teacher.objects.all().order_by('full_name')

    context = {
        'teachers': teacher_list
    }

    return render(request, 'teacher/list.html', context)
