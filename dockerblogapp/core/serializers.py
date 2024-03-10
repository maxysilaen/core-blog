from rest_framework import serializers

from .models import (
    Post
)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content',
                  'created_date', 'updated_date', 'user')
        read_only_fields = ('id', 'created_date', 'user')