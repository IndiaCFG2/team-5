from django.urls import path
from . import views 

app_name = 'students'

urlpatterns = [
	path('login', views.student_login, name='student_login'),
]