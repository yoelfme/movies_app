from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25, null=True)
    class Meta:
        db_table = 'categories'
    def __str__(self):
        return self.name

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
    def __str__(self):
        return '%s | %s | %s | %s | %s | %s | %s | %s | %s' % (
            self.category,
            self.name,
            self.video_url,
            self.description,
            self.image,
            self.duration,
            self.year,
            self.clasification,
            self.type
        )

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
    def __str__(self):
        return '%s | %s | %s | %s ' % (
            self.name,
            self.last_name,
            self.email,
            self.type
        )

class Subscription(models.Model):
    day = models.CharField(max_length=25, null=True)
    amount = models.IntegerField()
    card_id_number = models.IntegerField()
    expiration_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'subscriptions'
    def __str__(self):
        return '%s | %s | %s | %s | %s' % (
            self.day,
            self.amount,
            self.card_id_number,
            self.expiration_date,
            self.user
        )
