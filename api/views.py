from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie
from .serializers import MovieSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/movies-list/',
        'Detail View': '/movies-list/<str:pk>/',
        'Create': '/movie-create/',
        'Update': '/movie-update/<str:pk>/',
        'Delete': '/movie-delete/<str:pk>/',
    }
    
    return Response(api_urls)


@api_view(['GET'])
def movies_list(request):
    # Retrieve all movies from the database
    movies = Movie.objects.all()
    
    # Serialize the queryset using MovieSerializer
    serializer = MovieSerializer(movies, many=True)
    
    # Return the serialized data in a Response object with status code 200 (OK)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail(request):
    pass