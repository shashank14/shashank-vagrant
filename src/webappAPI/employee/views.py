from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from .serializers import EmployeeSerializer

from .models import Employee

class EmployeeApiView(APIView):

    #serializer_class = EmployeeSerializer

    def get(self,request,format=None):
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs,many=True)
        return Response(serializer.data)





# class EmployeeApiView(APIView):
#
#     serializer_class = EmployeeSerializer
#
#     def get(self,request,format=None):
#         ls = ['shashank','ragireddy','100']
#         return Response({'msg':'Hello Api View','ls':ls})
#
#     def post(self,request,format=None):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             name = serializer.data.get('name')
#             num = serializer.data.get('num')
#             role = serializer.data.get('role')
#             ls1  = [name,num,role]
#             return Response({'msg':'Hello Api View','Employee':ls1})
#         else:
#             return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
#
#     def put(self,request,pk=None):
#         serializer = EmployeeSerializer(data=request.data)
#         return Response({'msg':'Hello Api View put'})
#
#     def patch(self,request,pk=None):
#         serializer = EmployeeSerializer(data=request.data)
#         return Response({'msg':'Hello Api View patch'})
#
#     def delete(self,request,pk=None):
#         return Response({'msg':'Hello Api View delete'})
