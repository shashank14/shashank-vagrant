import requests
import json
BASE_URL='http://127.0.0.1:9090/'
# ENDPOINT='student/jsonx/'
ENDPOINT='movies/'
# resp=requests.get(BASE_URL+ENDPOINT)
# print(resp.json())

def get_resource():
    resp=requests.get(BASE_URL+ENDPOINT)
    # print(type(resp))
    print(resp.status_code)
    print(resp.json())
    # print(type(resp.json()))
    # print(type(resp))


get_resource()

def put_resource():
    resp=requests.put(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())

put_resource()

def post_resource():
    resp=requests.post(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())

post_resource()


def delete_resource():
    resp=requests.delete(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())

delete_resource()


# def get_resource(id):
#     resp=requests.get(BASE_URL+ENDPOINT+id+'/')
#     print(resp.status_code)
#     print(resp.json())
# def get_all():
#     resp=requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
# def create_resource():
#     new_emp={
#     'eno':700,
#     'ename':'Katrina',
#     'esal':7000,
#     'eaddr':'Mumbai',
#     }
#     resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# def update_resource(id):
#     new_emp={
#     'esal':70,
#     'eaddr':'Delhi',
#     }
#     resp=requests.put(BASE_URL+ENDPOINT+str(id)+'/',data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# def delete_resource(id):
#     resp=requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
#     print(resp.status_code)
#     print(resp.json())
# delete_resource(6)
