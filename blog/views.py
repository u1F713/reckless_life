#from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from .serializers import *

# Create your views here.


def say_hello(request):
    data = {"message": "Hello world, Mashu here ✌🏻"}
    return JsonResponse(data)


class ArticlesView(APIView):
    def get(self, request, *arg, **kwargs):
        if "name" in kwargs:
            try:
                query_set = models.Article.objects.get(url=kwargs['name'])
                return Response(ArticleSerializer(query_set, many=False).data)
            except:
                return Response({"err": "Post not found"})
        query_set = models.Article.objects.all()
        serialize = ArticleSerializer(query_set, many=True)
        return Response(serialize.data)