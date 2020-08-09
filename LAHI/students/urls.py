from django.urls import path
from . import views 

app_name = 'students'

urlpatterns = [
	path('login', views.student_login, name='student_login'),
	path('materials', views.materials, name='materials'),
	path('dashboard', views.dashboard, name='dashboard'),
	path('agenda', views.agenda, name='agenda'),
]