from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('index/', views.index, name='index'),  # Route to the index view
    path('about/', views.about, name='about'),  # Route to the about view
    path('debug/', views.debug, name='debug'),  # Route to the about view
    path('flightInfo/', views.flightInfo, name='flightInfo'),  # Route to the about view
]