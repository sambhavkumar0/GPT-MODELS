from django.urls import path

from . import views

urlpatterns=[
    path('',views.page1, name='page1'),
    path('result',views.resultpage, name='result'),

   
   





]