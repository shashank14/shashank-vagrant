from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
# Create your views here.
import json



from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



@method_decorator(csrf_exempt,name='dispatch')
class JsonCbv(View):

    def get(self,request,*args,**kwargs):
        # movie_dat = {
        # 'movie_name': 'The GodFather',
        # 'year':'1972',
        # 'director': 'Francis Ford Coppola'
        # }
        # return JsonResponse(movie_dat)

        resp = json.dumps({'msg':'This is from get method'})
        return HttpResponse(resp,content_type='application/json')

    def post(self,request,*args,**kwargs):
        resp = json.dumps({'msg':'This is from post method'})
        return HttpResponse(resp,content_type='application/json')

    def put(self,request,*args,**kwargs):
        resp = json.dumps({'msg':'This is from put method'})
        return HttpResponse(resp,content_type='application/json')

    def delete(self,request,*args,**kwargs):
        resp = json.dumps({'msg':'This is from delete method'})
        return HttpResponse(resp,content_type='application/json')


from .mixins import HttpResponseMixin

@method_decorator(csrf_exempt,name='dispatch')
class MovieJsonCbv(View,HttpResponseMixin):

    def get(self,request,*args,**kwargs):
        movie_dat = {
        'movie_name': 'The GodFather',
        'year':'1972',
        'director': 'Francis Ford Coppola'
        }

        return self.render_http_respose(movie_dat)


        # return JsonResponse(movie_dat)
        #
        # resp = json.dumps({'msg':'This is from get method'})
        # return HttpResponse(resp,content_type='application/json')

    def post(self,request,*args,**kwargs):
        # resp = json.dumps({'msg':'This is from post method'})
        # return HttpResponse(resp,content_type='application/json')
        return self.render_http_respose({'msg':'This is from post method'})

    def put(self,request,*args,**kwargs):
        # resp = json.dumps({'msg':'This is from put method'})
        # return HttpResponse(resp,content_type='application/json')
        return self.render_http_respose({'msg':'This is from put method'})

    def delete(self,request,*args,**kwargs):
        # resp = json.dumps({'msg':'This is from delete method'})
        # return HttpResponse(resp,content_type='application/json')

        return self.render_http_respose({'msg':'This is from delete method'})
