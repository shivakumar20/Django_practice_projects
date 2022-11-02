from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("all_emp",views.all_emp,name='home'),
    path("add_emp",views.add_emp,name='home'),
    path("remove_emp",views.remove_emp,name='home'),
    path("filter_emp",views.filter_emp,name='home'),
    
]
