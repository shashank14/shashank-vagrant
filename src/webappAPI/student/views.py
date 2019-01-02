from django.shortcuts import render
from django.http import HttpResponse

import json
# Create your views here.

def student_data_view(request):
    student_data = {
    'snum': 100,
    'sname': 'shashank',
    'sadd':'hyd'
    }
    resp = '<h1>Student Name : {} <br> Student Number : {}</h1>'.format(student_data['sname'],student_data['snum'])
    #return HttpResponse("<h1>HH</h1>")
    print(type(resp))
    return HttpResponse(resp)



def student_data_json_view(request):
    student_data = {
    'snum': 100,
    'sname': 'shashank',
    'sadd':'hyd'
    }
    print('json')
    resp = json.dumps(student_data)
    return HttpResponse(resp,content_type='application/json')

from django.http import JsonResponse
def student_data_json_view_two(request):
    student_data = {
    'snum': 100,
    'sname': 'shashank',
    'sadd':'hyd'
    }
    return JsonResponse(student_data)
