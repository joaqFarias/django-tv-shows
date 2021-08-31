from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required
from app_tv_shows.models import *

def root(request):
    return redirect('/shows')

def shows(request):

    shows = Show.objects.all()
    context = {
        'libros': shows,
    }
    context = {
        'shows': shows
    }
    return render(request, 'shows.html', context)

def show(request, id):
    
    show_id = Show.objects.get(id=int(id))
    context = {'show': show_id}

    return render(request, 'view_show.html', context)

def new(request):
    if request.method == 'POST':
        show_new = Show.objects.create(title=request.POST['title'], network=request.POST['network'], 
                                        release_date=request.POST['release_date'], description=request.POST['description'])
        show_new.save()

        return redirect(f"/shows/{show_new.id}")
    return render(request, 'new.html')

def edit(request, id):
    show_id = Show.objects.get(id=int(id))

    if request.method == 'POST':
        print(request.POST)
        for campo in request.POST.keys:
            if request.POST[campo] == '':
                print(vars(show_id)[campo])
                request.POST[campo] = vars(show_id)[campo]

        show_new = Show.objects.create(title=request.POST['title'], network=request.POST['network'], 
                                        release_date=request.POST['release_date'], description=request.POST['description'])
        show_new.save()

        return redirect(f"/shows/{show_new.id}")

    context = {'show': show_id}

    return render(request, 'edit.html', context)

def delete(request, id):
    show_id = Show.objects.get(id=int(id))
    show_id.delete()

    return redirect('/shows')
    
