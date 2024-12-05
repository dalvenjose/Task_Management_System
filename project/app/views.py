from django.shortcuts import render
from rest_framework .response import Response   
from rest_framework.decorators import api_view
from .serializer import *
from .models import *


# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])

def taskhome(request):
    if request.method == 'GET':
        objtask = task.objects.all()
        serializer = taskSerializer(objtask,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = taskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = task.objects.get(id=data['id'])
        serializer = taskSerializer(obj,data=data,partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj = task.objects.get(id=data['id'])
        serializer = taskSerializer(obj,data=data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else :
        data = request.data
        obj = task.objects.get(id=data['id'])
        obj.delete()
        return Response({"message":"deleted"})