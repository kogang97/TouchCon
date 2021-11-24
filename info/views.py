from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from info.models import Info
from info.serializers import InfoSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def info_list(request):
    if request.method == 'GET':
        info = Info.objects.all()
        info_serializer = InfoSerializer(info, many=True)
        del info_serializer.data[0]['pk']
        return JSONResponse(info_serializer.data)
