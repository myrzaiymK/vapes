from django.shortcuts import render ,redirect
from .models import Product
from .forms import ContactForm

def main(request):
    template_name = 'main/index.html'
    context = {}
    context['product'] = Product.objects.all()
    return render(request,template_name,context)
def contact(request):
    template_name = 'main/contact.html'
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else :
        form = ContactForm()
        context['form'] = form
    return render(request,template_name,context)

def shoes(request):
    template_name = 'main/shoes.html'
    context = {}
    context['product'] = Product.objects.all()
    return render(request,template_name,context)
def collection(request):
    template_name = 'main/collection.html'
    context = {}
    context['product'] = Product.objects.all()
    return render(request,template_name,context)
def racing_boots(request):
    template_name = 'main/racing_boots.html'
    context = {}
    context['product'] = Product.objects.all()
    return render(request,template_name,context)



# Create your views here.
