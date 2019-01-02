from django.conf.urls import url
from .views import student_data_view,student_data_json_view,student_data_json_view_two

urlpatterns = [
url(r'^$',student_data_view,name='allstudents'),
url(r'^json/$',student_data_json_view,name='allstudentsjson'),
url(r'^jsonx/$',student_data_json_view_two,name='allstudentsjsontwo'),
]
