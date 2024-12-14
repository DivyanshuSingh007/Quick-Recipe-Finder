from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('shahi_paneer',views.paneer),
    path('dal_makhani',views.dal),
    path('masala_tea',views.tea)
]