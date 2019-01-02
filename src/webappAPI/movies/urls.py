from django.conf.urls import url
from .views import JsonCbv,MovieJsonCbv


urlpatterns = [
url(r'^$',MovieJsonCbv.as_view(),name="movie"),
]
