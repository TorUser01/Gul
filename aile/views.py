from django.shortcuts import render
from django.views.generic import DetailView

from .models import *

def aileView(request):
    context = {
        'families': Aile.objects.all()
    }

    return render(request, 'Aile/aile.html', context)


class aileDetail(DetailView):
   model = Aile
   context_object_name = 'family'
   template_name = 'Aile/aile_detail.html'