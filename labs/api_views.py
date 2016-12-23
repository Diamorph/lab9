import json
from django.shortcuts import render, get_object_or_404 ,render_to_response
from labs.models import Restaurants
from .forms import Restaurants_Form
from django.contrib import auth
import os
from project import settings
from django.shortcuts import render_to_response ,redirect , HttpResponse #render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def add(request):
    result = "OK!"
    error_api = "Error"
    if request.method == "POST" and request.POST['name'] and request.POST['rate'] and request.POST['check'] and request.POST['city']and request.FILES['image']:
        rest = Restaurants.objects.create(name=request.POST['name'],
                                  rate=request.POST['rate'],
                                  check=request.POST['check'],
                                  city=request.POST['city'],
                                  date='2016-10-12',
                                  image=request.FILES['image'],
                                  )
        response_data = rest.dict()
        request.session['has_posted_already'] = True
        return HttpResponse(json.dumps({'restaurants': response_data}), content_type="application/json")
    return HttpResponse(json.dumps({'Status': 'error2'}), content_type="application/json")


def rest_get(request):
    if request.method == "GET":
        return HttpResponse(json.dumps([i.dict() for i in Restaurants.objects.all()]), content_type='application/json')

def upload_file(f):
    with open(os.path.join(settings.MEDIA_ROOT,f.name),'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def Restaurant_id(request,id):
    if request.method == "GET":
        return HttpResponse(json.dumps(Restaurants.objects.get(id=int(id)).dict()), content_type='application/json')


def delete(request,id):
    result = "Successful del"
    if request.method == "POST":
        rest = Restaurants.objects.get(id=int(id))
        Restaurants.objects.get(id=int(id)).delete()
        response_data = rest.dict()
        request.session['has_deleted_already'] = True
        return HttpResponse(json.dumps({'restaurants': response_data}), content_type="application/json")
    return HttpResponse(json.dumps({'Status': 'error2'}), content_type="application/json")

def search(request):
    rests = Restaurants.objects.none()
    flag = True
    if request.method == "GET":
        if 'search' in request.GET:
            search = request.GET['search'].split()
            for val in search:
                if flag:
                    newrests = Restaurants.objects.filter(name__icontains=val)
                    if newrests:
                        rests = newrests
                    else:
                        continue
                    flag = False
    return render(request, "Restaurants.html", {'restaurants': rests, 'user' : request.user})

def show_user(request):
    user = request.user
    if request.method == "GET" and request.user.is_superuser:
        return render(request , "users.html" , {'users' : User.objects.all() , 'user' : request.user})
    else:
        return render(request, "users.html", {'user':request.user,'users': User.objects.all(), 'user' : request.user})