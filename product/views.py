from django.shortcuts import render
from .models import Product

def main(request):
    template_name = 'main/index.html'
    context = {}
    context['product'] = Product.objects.all()
    return render(request,template_name,context)
def contact(request):
    template_name = 'main/contact.html'
    context = {}
    context['product'] = Product.objects.all()
    return render(request,template_name,context)

# Create your views here.
