from django.http import HttpResponse
import json


class HttpResponseMixin(object):

    def render_http_respose(self,data):
        json_data = json.dumps(data)
        return HttpResponse(json_data,content_type='application/json')
