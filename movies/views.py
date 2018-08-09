from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

from .models import User, Movie

def users_list(request):
    if request.method == 'GET':
        MAX_OBJECTS = 20
        users = User.objects.all()[:20]
        data = {"results": list(users.values("id", "name", "last_name", "email", "type", "password"))}
        return JsonResponse(data)
    elif request.method == 'POST':


        return JsonResponse({"message": "hola"})

        # user = User(
        # name = request.POST['name'], 
        # last_name = request.POST['last_name'], 
        # email = request.POST['email'], 
        # type = request.POST['type'], 
        # password = request.POST['password'])
        # user.save()
        # return Response(user, status=status.HTTP_201_CREATED)

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
