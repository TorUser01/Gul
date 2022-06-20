from django.urls import path
from .views import *
urlpatterns = [
    path('ruh', ruhView, name='ruh'),
    path('ruh/<slug:slug>/', RuhDetail.as_view(), name='ruh_detail')

]