from django.contrib import admin
from django.urls import path
from aviation import views
urlpatterns = [
    path('', views.home,name = 'home'),
    path('result', views.result,name = 'result'),
]
