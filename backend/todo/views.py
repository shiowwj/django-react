from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .serializers import ShoppingSerializer
from .models import Todo
from .models import Shopping


#provides implementation for CRUD operations by default.
#below, we are specifying class and the query set

class TodoView(viewsets.ModelViewSet):
	serializer_class = TodoSerializer
	queryset = Todo.objects.all()
	print('QUERYYYYSET',queryset[0].__dict__)
# Create your views here.

class ShoppingView(viewsets.ModelViewSet):
	serializer_class = ShoppingSerializer
	queryset = Shopping.objects.all()