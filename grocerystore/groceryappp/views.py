from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Grocery_form
from .models import Grocery
# Create your views here.
def additem(request):
    if request.method=="POST":
        form=Grocery_form(request.POST)
        if form.is_valid():
            newitem=form.save(commit=False)
            newitem.name=form.cleaned_data["name"]
            newitem.type=form.cleaned_data["type"]
            newitem.quantity=form.cleaned_data["quantity"]
            newitem.rate=form.cleaned_data["rate"]
            newitem.amount=newitem.quantity*newitem.rate
            newitem.save()
            return HttpResponseRedirect('./display')
        else:
            form=Grocery_form(request.POST)
            return render(request, 'additem.html', {'form': form})
    else:
        form=Grocery_form(request.POST)
        return render(request, 'additem.html', {'form': form})
def display(request):
    items=Grocery.objects.all()
    return render(request,'homepage.html', {'req':request, 'items':items}) 
