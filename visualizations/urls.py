from django.urls import path
from . import views

urlpatterns = [
        path('', views.plotly, name='plotly'),
	path('ex1', views.ex1, name='ex1'),
]
