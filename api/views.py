from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
 
# Create your views here.
class TodoView(viewsets.ModelViewSet):
     queryset = Todo.objects.all().order_by('is_done','-updated_at')
     serializer_class = TodoSerializer


class CustomView(APIView):

     @api_view(['GET'])
     def count_pending_tasks(request):
        count = len(set(Todo.objects.filter(is_done=False)))
        return Response({'count': count})   