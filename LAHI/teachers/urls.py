from django.urls import path
from . import views 

app_name = 'teachers'

urlpatterns = [
	path('login', views.teacher_login, name='teacher_login'),
	path('uploadfiles', views.upload_files, name='upload_files'),
	path('materials', views.materials, name='materials'),
    path('createstudent', views.create_student, name='create_student'),
	path('dashboard', views.dashboard, name='dashboard'),
	path('agenda', views.agenda, name='agenda'),
]