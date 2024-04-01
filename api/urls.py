from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('movies-list/', views.movies_list, name='movies-list'),
    path('movies-list/<str:pk>/', views.movie_detail, name='movie-detail'),
    path('movie-create/', views.movie_create, name='movie-create'),
    path('movie-update/<str:pk>/', views.movie_update, name='movie-update'),
    path('movie-delete/<str:pk>/', views.movie_delete, name='movie-delete'),
]