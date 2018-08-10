from movies.models import User, Movie
from movies.serializers import UserSerializer, MovieSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

class UserList(APIView):
    """
    List all users of our application
    """
    def get(self, request, format=None):
        # Search users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

class MoviesList(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)

class CreateSubscription(APIView):
    def post(self, request, format=None, user_id=None):
        query = User.objects.all()

        user = get_object_or_404(query, pk=user_id)
        user.type = 'PREMIUM'
        user.save()

        return Response(status=status.HTTP_200_OK)

def movies_list(request):
    MAX_OBJECTS = 20
    movies = Movie.objects.all()[:20]
    data = {"results": list(movies.values(
        "id",
        "category",
        "name",
        "video_url",
        "description",
        "image",
        "duration",
        "year",
        "clasification",
        "type",
        "image"
        ))}
    return JsonResponse(data)
