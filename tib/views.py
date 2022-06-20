from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.core.paginator import Paginator
from .models import *






def tibView(request):
   keyword = request.GET.get('keyword')
   if keyword:
      tibs = Tib.objects.filter(Q(name__contains=keyword))
      return render(request, 'Tib/tib.html', {'tibs': tibs})

   tibs = Tib.objects.all()
   paginator = Paginator(tibs, 10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   context = {
      'tibs': page_obj,
      'categories': TibCategory.objects.all(),
   }
   return render(request, 'Tib/tib.html', context)





def tib_view_with_category(request, slug, *args, **kwargs):
   keyword = request.GET.get('keyword')
   categories = TibCategory.objects.all()
   if keyword:
      tibs = Tib.objects.filter(name__contains=keyword)
      return render(request, 'Tib/tib_slug.html', {'tibs': tibs, 'categories': categories})

   tibCategory = TibCategory.objects.get(slug=slug)
   tibs = tibCategory.tib_set.filter(active=True)
   paginator = Paginator(tibs, 10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   context = {
      'tibs': page_obj,
      'categories': categories,

   }
   return render(request, 'Tib/tib_slug.html', context)





class tibDetail(DetailView):
   model = Tib
   context_object_name = 'tib'
   template_name = 'Tib/tib_detail.html'




