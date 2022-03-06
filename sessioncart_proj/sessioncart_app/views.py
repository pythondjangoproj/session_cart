from django.shortcuts import render
from .forms import AddItemForm
# Create your views here.

def add_item_view(request):
    form=AddItemForm()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(120)
    return render(request,'sessioncart_app/additem.html',{'form':form})

def display_item(request):
    return render(request,'sessioncart_app/displayitem.html')
