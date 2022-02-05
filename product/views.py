from django.shortcuts import render ,redirect,get_object_or_404
from .models import Product
from .forms import ContactForm
from .cart import Cart
from .forms import CartAddProductForm


def main(request):
    template_name = 'siteKG/index.html'
    context = {}
    context['product'] = Product.objects.all()[:6]
    return render(request,template_name,context)


def detail(request,id):
    context = {}
    template_name = 'siteKG/detail.html'
    context["product"] = Product.objects.get(id=id)
    return render(request, template_name, context)

def contact(request):
    template_name = 'siteKG/contact.html'
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
    template_name = 'siteKG/shoes.html'
    context = {}
    context['product'] = Product.objects.all()[:6]
    return render(request,template_name,context)
def collection(request):
    template_name = 'siteKG/collection.html'
    context = {}
    context['product'] = Product.objects.all()
    return render(request,template_name,context)
def racing_boots(request):
    template_name = 'siteKG/racing_boots.html'
    context = {}
    context['product'] = Product.objects.all()
    return render(request,template_name,context)
# def cart_add(request,product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product,id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['update'])
#     return redirect('cart:cart_detail')
#
# def cart_remove(request,product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('cart:cart_detail')
#
# def cart_detail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['udate_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
#                                                                   'update': True})
#         return render(request, 'cart/detail.html',{'cart':cart})


def cart(request, id):
    template_name = 'siteKG/collection.html'
    product = Product.objects.get(id=id)
    cart = Cart
    final_sum = cart.objects.create().aggregate(sum(product.price))
    return render(request,template_name)

# Create your views here.
