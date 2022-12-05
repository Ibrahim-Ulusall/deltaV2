from django.shortcuts import render
from .models import LessonModels
# Create your views here.

def index(request):
    return render(request,'lessons/index.html',{
        'lessons':LessonModels.objects.all()
    })
