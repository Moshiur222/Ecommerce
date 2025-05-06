from django.shortcuts import render
from store.views import *

# Create your views here.

def sing_in(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request,'signin.html',context)

def sing_up(request):
    context = {}
    return render(request,'signup.html',context)