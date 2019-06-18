"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views
# from shopping import views

print ('hello',views)
router = routers.DefaultRouter()
print('OVHER HERE', router)
router.register(r'todos', views.TodoView, 'todo')
router.register(r'shoppings', views.ShoppingView, 'shopping')

#this step completes the building of the API.WE CAN NOW PERFORM CRUD operations on the Todo model.
#router class allows us to make the following queries:
#/todos/ -> returns a list of all the Todo items (create and read can be done here)
#/todos/id -> returns a single Todo item using id primary key (update and delete done here)

urlpatterns = [
    path('admin/', admin.site.urls), path('api/', include(router.urls))
]