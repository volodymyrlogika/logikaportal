from django.shortcuts import render
from .models import Grade

# Create your views here.
def grade_diary_home(request):
    grades = Grade.objects.filter(student=request.user)
    return render(request, 'grade_diary/home.html', {'grades': grades})