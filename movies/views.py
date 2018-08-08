from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import User, Movie

def users_list(request):
    MAX_OBJECTS = 20
    users = User.objects.all()[:20]
    data = {"results": list(users.values("id", "name", "last_name", "email", "type", "password"))}
    return JsonResponse(data)

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
