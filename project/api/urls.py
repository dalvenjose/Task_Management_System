from django.urls import path
from app.views import *



urlpatterns = [
    path('task' ,taskhome , name='task'),
]