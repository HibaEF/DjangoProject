from django.urls import path
from .views import homePage, student_list,coach_list,student_details,StudentListView
urlpatterns = [
    path('home/',homePage , name="home"),
    path('listStudent/',student_list,name='listStudent'),
    path('listCoach/',coach_list,name='listCoach'),
    path('st_details/<int:id>',student_details),
   path('listStudents/',StudentListView.as_view(),name='listStudent1')
]
