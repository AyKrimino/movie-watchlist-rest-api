from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie
from .serializers import MovieSerializer


@api_view(['GET'])
def api_overview(request):
    '''
    Provide an overview of available movie-related API endpoints.

    :param request: HTTP request object.
    :return: Response with a dictionary of available API endpoints.
    '''
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
    '''
    Retrieve a list of all movies.

    :param request: HTTP request object.
    :return: Response with serialized list of movies and 200 OK if successful.
    '''
    # Retrieve all movies from the database
    movies = Movie.objects.all()
    
    # Serialize the queryset using MovieSerializer
    serializer = MovieSerializer(movies, many=True)
    
    # Return the serialized data in a Response object with status code 200 (OK)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail(request, pk):
    '''
    Retrieve a specific movie detail.

    :param request: HTTP request object.
    :param pk: Primary key of the movie to retrieve.
    :return: Response with serialized movie detail or 404 if movie does not exist.
    '''
    try:
        # Retrieve the movie object by its primary key
        movie = Movie.objects.get(id=pk)
    except Movie.DoesNotExist:
        # If movie does not exist, return 404 Not Found response
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    # Serialize the movie object
    serializer = MovieSerializer(movie)

    # Return the serialized data in a Response object with status code 200 (OK)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def movie_create(request):
    '''
    Create a new movie.

    :param request: HTTP request object containing movie data in the request body.
    :return: Response with serialized movie data or 400 Bad Request if data is invalid.
    '''
    # serialize the request data
    serializer = MovieSerializer(data=request.data)
    
    # Check if serialization is valid
    if serializer.is_valid():
        # Save the serialized data and return as response
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        # Return 400 Bad Request response if serialization is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def movie_update(request, pk):
    '''
    Update an existing movie.

    :param request: HTTP request object containing the updated movie data.
    :param pk: Primary key of the movie to be updated.
    :return: Response with serialized movie data if successful, or 404 Not Found if movie does not exist.
    '''
    try:
        # Get the movie instance to be updated
        movie = Movie.objects.get(pk=pk)
        print(movie)
        
        # Serialize the updated movie data
        serializer = MovieSerializer(instance=movie, data=request.data)
        
        # Check if serialization is valid
        if serializer.is_valid():
            # Save the updated movie data
            serializer.save()
            # Return serialized movie data with status 200 OK
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Return validation errors with status 400 Bad Request
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Movie.DoesNotExist:
        # Return 404 Not Found if movie does not exist
        return Response({'error': 'Movie not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['DELETE'])
def movie_delete(request, pk):
    '''
    Delete an existing movie.

    :param request: HTTP request object containing the movie data to be deleted.
    :param pk: Primary key of the movie to be deleted.
    :return: Response with success message if movie is deleted successfully, or 404 Not Found if movie does not exist.
    '''
    try:
        # Get the movie instance to be deleted
        movie = Movie.objects.get(pk=pk)

        # Delete the movie
        movie.delete()
        
        # Return success message with status 200 OK
        return Response({'detail': 'Movie deleted successfully.'}, status=status.HTTP_200_OK)
    except Movie.DoesNotExist:
        # Return 404 Not Found if movie does not exist
        return Response({'error': 'Movie not found.'}, status=status.HTTP_404_NOT_FOUND)