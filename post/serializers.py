from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

# class PostSerializer(serializers.Serializer):
#     category_id = serializers.IntegerField()
#     title = serializers.CharField(max_length=100)
#     body = serializers.CharField()
#     created_at = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.category_id = validated_data.get("category_id", instance.category_id)
#         instance.title = validated_data.get("title", instance.title)
#         instance.body = validated_data.get("body", instance.body)
#         instance.save()
#         return instance
