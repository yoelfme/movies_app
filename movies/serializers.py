from rest_framework import serializers
from movies.models import User, Category, Movie

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=True, max_length=100)
    last_name = serializers.CharField(required=True, allow_blank=True, max_length=100)
    email = serializers.EmailField(required=True, max_length=100)
    type = serializers.CharField(required=False, allow_blank=True, max_length=100)
    password = serializers.CharField(required=True, max_length=100)

    class Meta:
        model = User

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)

    class Meta:
        model = Category

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = CategorySerializer(read_only=True)
    name = serializers.CharField(max_length=50, allow_blank=True)
    video_url = serializers.CharField(max_length=200, allow_blank=True)
    description = serializers.CharField(max_length=200, allow_blank=True)
    image = serializers.CharField(max_length=200, allow_blank=True)
    duration = serializers.CharField(max_length=25, allow_blank=True)
    year = serializers.CharField(max_length=10, allow_blank=True)
    clasification = serializers.CharField(max_length=25, allow_blank=True)
    type = serializers.CharField(max_length=200, default="FREE")

    class Meta:
        model = Movie
