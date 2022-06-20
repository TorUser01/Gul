from django.urls import path
from .views import *
urlpatterns = [
    path('', indexView, name='index'),
    path('maarip', maaripView, name='maarip'),
    path('maarip/<slug:slug>/', MaaripDetail.as_view(), name='maarip_detail'),
    path('maarip-category/<slug:slug>', maarip_view_with_category, name='maarip_view_with_category'),
    path('contact', contactView, name='contactView'),
    path('contuctView', Contactview.as_view(), name='Contactview'),
]