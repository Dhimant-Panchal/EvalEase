from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Assignment, Module, Submission, Keyword


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["code", "title"]


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ["id", "title", "due_date"]
