from django.conf.urls import url

from .views import EmployeeApiView

urlpatterns = [
url(r'^$',EmployeeApiView.as_view(),name='list'),
]
