from django.urls import path
from .views import *
urlpatterns = [

    path('tib', tibView, name='tib'),
    path('tib/<slug:slug>/', tibDetail.as_view(), name='tib_detail'),
    path('tib-category/<slug:slug>/', tib_view_with_category, name='tib_view_with_category')

]