from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogModel
from user.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    author_id = serializers.CharField()
    author = UserSerializer(read_only=True)
    class Meta:
        model = BlogModel
        fields = ["id", "title", "description", "created_at", "updated_at", "author", "author_id"]