from django.urls import path, include
from . import  views

app_name = 'todo'
urlpatterns = [
    path('vonly/', views.TodoVueOnlyTV.as_view(), name='vonly'),
]
