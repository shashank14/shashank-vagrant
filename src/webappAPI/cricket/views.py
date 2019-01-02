from django.shortcuts import render

from .models import CricketTeamModel
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.

from django.core.serializers import serialize
import json

from .mixins import SerializeMixin,HttpResponseMixin

class CricketTeamsView(View):

    def get(self,request,*args,**agrs):

        # team = CricketTeamModel.objects.get(team_id=3)
        # json_data = serialize('json',[team,])
        # return HttpResponse(json_data,content_type='application/json')


        # team = CricketTeamModel.objects.get(team_id=3)
        # json_data = serialize('json',[team,],fields=('team_captain',))
        # return HttpResponse(json_data,content_type='application/json')

        team = CricketTeamModel.objects.all()
        json_data = serialize('json',team)
        return HttpResponse(json_data,content_type='application/json')


class CricketTeamsViewX(View):

    def get(self,request,*args,**agrs):

        team = CricketTeamModel.objects.all()
        json_data = serialize('json',team)
        p_dict = json.loads(json_data)
        print(p_dict)
        final_data = []
        for obj in p_dict:
            emp_data = obj['fields']
            final_data.append(emp_data)

        json_data = json.dumps(final_data)
        return HttpResponse(json_data,content_type='application/json')



class CricketTeamsViewXJ(View,SerializeMixin):

    def get(self,request,*args,**agrs):

        team = CricketTeamModel.objects.all()
        json_data = self.serialize_cricket_teams(team)
        return HttpResponse(json_data,content_type='application/json')




class CricketTeamView(View,SerializeMixin,HttpResponseMixin):

    def get(self,request,id,*args,**agrs):

        try:
            team = CricketTeamModel.objects.get(team_id=id)
        except CricketTeamModel.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resource not available'})
            return self.render_to_http_response(json_data,status=404)
            #return HttpResponse(json_data,content_type='application/json',status=404)
        else:
            json_data = self.serialize_cricket_team(team)
            return self.render_to_http_response(json_data)
            #return HttpResponse(json_data,content_type='application/json',status=200)

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .utils import is_json

@method_decorator(csrf_exempt,name='dispatch')
class CricketTeamsCBV(View,SerializeMixin):

    def get(self,request,*args,**agrs):

        team = CricketTeamModel.objects.all()
        json_data = self.serialize_cricket_teams(team)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data = request.body
        valid_json = is_valid(json_data)
        if valid_json:
            print("True")
        else:
            resp = json.dumps({'msg':'Please send valid json only'})
            return HttpResponse(resp,content_type='application/json')
