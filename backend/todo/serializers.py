from rest_framework import serializers
from .models import Todo
from .models import Shopping

#tells the model to work with the fields we want to be converted to JSON (serializers)

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = ('id', 'title', 'description', 'completed')

class ShoppingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Shopping
		fields = ('id', 'title', 'description', 'price', 'dateCreated', 'in_stock')