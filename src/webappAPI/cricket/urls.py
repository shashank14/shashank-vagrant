from django.conf.urls import url
from .views import CricketTeamsView,CricketTeamsViewX,CricketTeamsViewXJ,CricketTeamView,CricketTeamsCBV

urlpatterns = [
url(r'^$',CricketTeamsView.as_view(),name='teams'),
url(r'teams/$',CricketTeamsViewX.as_view(),name='teamsx'),
url(r'teamsx/$',CricketTeamsViewXJ.as_view(),name='teamsx'),
url(r'teamview/(?P<id>\d+)/$',CricketTeamView.as_view(),name='teamview'),
url(r'api/$',CricketTeamsCBV.as_view(),name='cricketteams'),
]
