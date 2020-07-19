from django.shortcuts import render
from .models import Portfolio, ProjectImage
from django.views.generic import DetailView

# Create your views here.
def home(request):
   portfolio = Portfolio.objects.all().order_by('?')
   context = {
      'portfolio':portfolio
   }
   return render(request, 'zahradeen/home.html', context)


def project_detail(request, pk, slug):
   portfolio = Portfolio.objects.get(pk=pk)
   images = ProjectImage.objects.filter(portfolio_id=pk)
   context= {
      'portfolio':portfolio,
      'images':images
   }
   return render(request, 'zahradeen/project_detail.html', context)

