
import json
from django.core.serializers import serialize
from django.http import HttpResponse

class SerializeMixin(object):

    def serialize_cricket_teams(self,data):
        json_data = serialize('json',data)
        p_dict = json.loads(json_data)
        print(p_dict)
        final_data = []
        for obj in p_dict:
            emp_data = obj['fields']
            final_data.append(emp_data)

        return json.dumps(final_data)

    def serialize_cricket_team(self,data):
        json_data = serialize('json',[data,])
        p_dict = json.loads(json_data)
        print(p_dict)
        final_data = []
        for obj in p_dict:
            emp_data = obj['fields']
            final_data.append(emp_data)

        return json.dumps(final_data)

class HttpResponseMixin(object):

    def render_to_http_response(self,data,status=200):
        return HttpResponse(data,content_type='application/json',status=status)
