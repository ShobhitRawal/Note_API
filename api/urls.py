from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteList.as_view()),
    
]