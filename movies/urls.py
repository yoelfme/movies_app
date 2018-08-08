# In views.py
def users_list(request):
    pass

def movies_list(request):
    pass

def users_detail(request, pk):
    pass

# in urls.py
from django.urls import path
from .views import users_list, movies_list
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", users_list, name="users_list"),
    path("movies/", movies_list, name="movies_list"),
]