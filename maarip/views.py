from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.core.paginator import Paginator
from .models import *
from .forms import *

def indexView(request):
   context = {
      'categories': MaaripCategory.objects.all()
   }
   return render(request, 'Home/index.html', context)



def maaripView(request):
   keyword = request.GET.get('keyword')
   if keyword:
      maarips = Maarip.objects.filter(Q(name__contains=keyword) | Q(category__maaripCategory__contains=keyword))
      return render(request, 'Maarip/maarip.html', {'maarips': maarips})

   maarips = Maarip.objects.all()
   paginator = Paginator(maarips, 10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   context = {
      'maarips': page_obj,
      'categories': MaaripCategory.objects.all(),
   }
   return render(request, 'Maarip/maarip.html', context)





def maarip_view_with_category(request, slug, *args, **kwargs):
   keyword = request.GET.get('keyword')
   categories = MaaripCategory.objects.all()
   if keyword:
      maarips = Maarip.objects.filter(Q(name__contains=keyword) | Q(category__maaripCategory__contains=keyword))
      return render(request, 'Maarip/maarip_slog.html', {'maarips': maarips, 'categories': categories})




   maaripCategory = MaaripCategory.objects.get(slug=slug)
   maarips = maaripCategory.maarip_set.filter(active=True)
   paginator = Paginator(maarips, 10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   context = {
      'maarips': page_obj,
      'categories': categories,

   }
   return render(request, 'Maarip/maarip_slog.html', context)





class MaaripDetail(DetailView):
   model = Maarip
   context_object_name = 'maarip'
   template_name = 'Maarip/maarip_detail.html'



def contactView(request):
   return render(request, 'Blonging/contact.html')


class Contactview(View):
   def get(self, request, *args, **kwargs):
      context = {
         'form': ContactForm()
      }
      return render(request, 'Blonging/basarili.html', context)

   def post(self, request, *args, **kwargs):
      form = ContactForm(request.POST or None)
      if form.is_valid():
         c_form = form.save(commit=False)
         c_form.save()
         return render(request, 'Blonging/basarili.html', context={'form': ContactForm()})