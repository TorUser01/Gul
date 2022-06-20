from django.urls import path
from .views import *
urlpatterns = [
    path('aile', aileView, name='aile'),
    path('aile/<slug:slug>/', aileDetail.as_view(), name='aile_detail')

]
