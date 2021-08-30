from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required

def root(request):
    return redirect('/shows')

def shows(request):

    context = {
        'saludo': 'Hola'
    }
    return render(request, 'shows.html', context)

def show(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'show.html', context)

def new(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'new.html', context)

def edit(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'edit.html', context)

