from django.shortcuts import render
from django.views.generic import DetailView

from .models import *
def ruhView(request):
    context = {
        'ruhs': Ruh.objects.all()[:1],
        'ruhss': Ruh.objects.all(),
    }
    return render(request, 'Ruh/ruh.html', context)




class RuhDetail(DetailView):
   model = Ruh
   context_object_name = 'ruh'
   template_name = 'Ruh/ruh_detail.html'