from rest_framework import serializers
from .models import Post
import uuid

class PostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content']

    def validate_title(self, value):
        existing_title = Post.objects.filter(title=value).exists()
        if existing_title:
            raise serializers.ValidationError("Title already exists")
        return value

    def validate_content(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("Content is too short")
        return value