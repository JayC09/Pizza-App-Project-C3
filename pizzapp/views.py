from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def index(request):
    p = pizza.objects.all()

    
    context = {'pizza': p,}
    return render(request, 'pizza/pizzalist.html', context)

def createPizza(request):
    p = pizza.objects.all()

    p_type =''
    p_size =''

    form = PizzaForm()

    if request.method == 'POST':
        form = PizzaForm(request.POST or None)
        
        if form.is_valid():
            p_type = form.cleaned_data.get("pizza_type")
            p_size = form.cleaned_data.get("pizza_size")
            if (p_type=="Regular" or p_type=="Square") and (p_size=="Small" or p_size=="Medium" or p_size=="Large"):
                form.save()
            return redirect('/')

    context = {'pizza': p, 'form':form}
    return render(request, 'pizza/create_pizza.html', context)


def updatePizza(request, pk):
    p = pizza.objects.get(id=pk)
    p_type =''
    p_size =''

    form = PizzaForm(instance=p)

    if request.method == 'POST':
        form = PizzaForm(request.POST, instance=p)
        if form.is_valid():
            p_type = form.cleaned_data.get("pizza_type")
            p_size = form.cleaned_data.get("pizza_size")
            if (p_type=="Regular" or p_type=="Square") and (p_size=="Small" or p_size=="Medium" or p_size=="Large"):
                form.save()
            return redirect('/')


    context = {'form': form}

    return render(request, 'pizza/update_pizza.html', context)

def deletePizza(request, pk):
    item = pizza.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'pizza/delete.html', context)

def showInfo(request):
    allp = pizza.objects.all()
    sorted_type = pizza.objects.order_by('pizza_type')
    sorted_size = pizza.objects.order_by('pizza_size')

    context = {'allPizzas': allp}

    return render(request, 'pizza/info_pizza.html', context)

def sortType(request):
    allp = pizza.objects.all()
    sorted_type = pizza.objects.order_by('pizza_type')

    context = {'sorted_type':sorted_type}

    return render(request, 'pizza/sortType.html', context)

def sortSize(request):
    allp = pizza.objects.all()
    sorted_size = pizza.objects.order_by('pizza_size')

    context = {'sorted_size':sorted_size}
    
    return render(request, 'pizza/sortSize.html', context)


        