from django.contrib import admin

# Register your models here.

from .models import Category
from .models import Movie
from .models import User
from .models import Subscription

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Subscription)