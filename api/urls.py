from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('movies-list/', views.movies_list, name='movies-list'),
]