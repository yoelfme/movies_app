from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25, null=True)
    class Meta:
        db_table = 'categories'

class Movie(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    video_url = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    image = models.CharField(max_length=200, null=True)
    duration = models.CharField(max_length=25, null=True)
    year = models.CharField(max_length=10, null=True)
    clasification = models.CharField(max_length=25, null=True)
    type = models.CharField(max_length=200, default="FREE")
    class Meta:
        db_table = 'movies'

class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(
        max_length=254,
        unique=True,
        db_index=True
    ) 
    type = models.CharField(max_length=200, default="BASIC")
    password = models.CharField(max_length=25, null=True)
    class Meta:
        db_table = 'users'

class Subscription(models.Model):
    day = models.CharField(max_length=25, null=True)
    amount = models.IntegerField()
    card_id_number = models.IntegerField()
    expiration_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'subscriptions'
