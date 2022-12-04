from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Task


class TaskModel:
    def __int__(self, title, content):
        self.title = title
        self.content = content


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=250)
    content = serializers.CharField()


def encode():
    model = TaskModel('Adam', 'Content: Adam Smith')
    model_sr = TaskSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)

