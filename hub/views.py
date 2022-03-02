from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Coach
from django.views.generic import ListView
# Create your views here.
def homePage(request): 
    return HttpResponse ("<h1> Welcome To The ... </h1>")
def student_list(request):
    list =Student.objects.all() #activer l orm de django 
    return render(
        request,
        'hub/index.html',
        {
            'students': list,
        }
    )
class StudentListView(ListView):
    model= Student
    template_name ="hub/index.html"
    paginate_by =2 #pour limité l'affichage en 2 etudiants seulement
class StudentDetailView(DetailView):
    model= Student


def student_details(request,id):
    student =Student.objects.get(id=id) #activer l orm de django 
    return render(
        request,
        'hub/st_details.html',
        {
            'student': student,
        }
    )

def coach_list(request):
    listC =Coach.objects.all() #activer l orm de django 
    return render(
        request,
        'hub/index.html',
        {
            'coachs': listC,
        }
    )