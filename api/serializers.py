from rest_framework import serializers
from .models import TodoModel

class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['id', 'todo_title', 'todo_description']

