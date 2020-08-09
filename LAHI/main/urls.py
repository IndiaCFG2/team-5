from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('download/<str:filename>', views.download, name='download'),
	path('logout', views.logout_view, name='logout')
]