from django.contrib import admin
from .models import Todo # add this
from .models import Shopping

class TodoAdmin(admin.ModelAdmin):  # add this
  list_display = ('title', 'description', 'completed') # add this

class ShoppingAdmin(admin.ModelAdmin):
	product_display = ('title', 'description', 'price', 'dateCreated', 'in_stock')



# Register your models here.
admin.site.register(Todo, TodoAdmin) # add this
admin.site.register(Shopping, ShoppingAdmin)