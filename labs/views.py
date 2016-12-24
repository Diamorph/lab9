from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 ,render_to_response, redirect
from .models import Restaurants
from django.contrib import auth
from .forms import Restaurants_Form
from django.contrib.auth.models import User
import os,json
from project import settings
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def rest(request):
    result = "Successful add!"
    if request.method == "POST" and request.POST['name'] and request.POST['rate'] and request.POST['check'] and request.POST['date'] and request.POST['city'] and request.FILES['image']:
        form = Restaurants_Form(request.POST, request.FILES)
        if form.is_valid():
            Restaurants.objects.create(name=request.POST['name'],
                                         rate=request.POST['rate'],
                                         check=request.POST['check'],
                                         city=request.POST['city'],
                                         date=request.POST['date'],
                                         image=request.FILES['image'])
        return render(request,"main.html", {'result': result, 'user' : request.user})
    else:
        if request.method == "GET":
            return render(request,"add.html", {'restaurants': Restaurants.objects.all(), 'user' : request.user})


def rest_get(request):
    if request.method == "GET":
        rest_list = Restaurants.objects.all()
        paginator = Paginator(rest_list, 3)
        page = request.GET.get('page')
        try:
            rest= paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            rest = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            rest = paginator.page(paginator.num_pages)
        return render(request,"Restaurants.html", {'restaurants': rest,'user' : request.user})
    elif request.method == "DELETE":
        Restaurants.objects.get(id=request.GET['rest']).delete()
        return HttpResponse(json.dumps({'status': 'ok'}), content_type="application/javascript")

def upload_file(f):
    with open(os.path.join(settings.MEDIA_ROOT,f.name),'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def Restaurant_id(request,id):
    if request.method == "GET":
        return render(request,"Restaurants.html" , {'restaurants': [Restaurants.objects.get(id = int(id))], 'user' : request.user})


def DelRestaurant(request,id):
    result = "Successful del"
    if request.method == "DELETE":
        Restaurants.objects.get(id=int(id)).delete()
        return HttpResponse(json.dumps({'status': 'ok'}) ,content_type="application/javascript")


def search(request):
    rests = Restaurants.objects.none()
    flag = True
    print(rests)
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
            else:
                newrests = Restaurants.objects.filter(name__icontains=val)
                if newrests:
                    rests = newrests

    return HttpResponse(json.dumps([i.dict() for i in rests ]), content_type="application/javascript")

# def search(request):
#     rests = Restaurants.objects.none()
#     flag = True
#     if request.method == "GET":
#         if 'search' in request.GET:
#             search = request.GET['search'].split()
#             for val in search:
#                 if flag:
#                     newrests = Restaurants.objects.filter(name__icontains=val)
#                     if newrests:
#                         rests = newrests
#                     else:
#                         continue
#                     flag = False
#         return render(request, "Restaurants.html", {'restaurants': rests, 'user' : request.user})

def show_user(request):
    user = request.user
    if request.method == "GET" and request.user.is_superuser:
        return render(request , "users.html" , {'users' : User.objects.all() , 'user' : request.user})
    else:
        return render(request, "users.html", {'user':request.user,'users': User.objects.all()})


def rest_get_user(request):
    user = request.user
    if request.method == "GET" and request.user.is_authenticated():
        return render(request, "Restaurants.html", {'restaurants': Restaurants.objects.all(), 'user': request.user})
    else:
        return HttpResponse("Please sign in")






# def search(request):
#     rests = Restaurants.objects.none()
#     flag = True
#     print(rests)
#     if 'search' in request.GET:
#         search = request.GET['search'].split()
#         print(search)
#         for val in search:
#             if flag:
#                 newrests = Restaurants.objects.filter(name__icontains=val)
#                 print(newrests)
#                 if newrests:
#                     rests = newrests
#                 else:
#                     continue
#                 flag = False
#             else:
#                 newrests = rests & Restaurants.objects.filter(name__icontains=val)
#                 if newrests:
#                     rests = newrests
#
#     return render(request, "Restaurants.html", {'restaurants': rests})



