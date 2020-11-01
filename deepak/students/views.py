from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student, Score
# Create your views here.

class StudentListView(ListView):
    
    template_name='students/student_list.html'
    
class StudentDetailView(DetailView):
    model=Student
    template_name='students/detail.html'





  