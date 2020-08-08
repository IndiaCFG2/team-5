from django.urls import path
from . import views 

app_name = 'teachers'

urlpatterns = [
	path('login', views.teacher_login, name='teacher_login'),
    
]