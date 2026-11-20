from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class RegisterSerializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['id','username','password','email']

    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model=NoteDb
        fields="__all__"

        read_only_fields=["id","user","created_date"]


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model=TaskDb
        fields="__all__"
        read_only_fields=["id","user","created_date"]
