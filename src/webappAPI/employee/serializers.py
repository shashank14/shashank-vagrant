from .models import Employee
from rest_framework import serializers



class EmployeeSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=10)
    num = serializers.IntegerField()
    role = serializers.CharField(max_length=10)
