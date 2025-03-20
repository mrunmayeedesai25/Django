from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponsePermanentRedirect 
from Home.forms import *
# Create your views here.
# def Home(request):

#     path = request.path
#     scheme = request.scheme
#     method = request.method 

#     # return HttpResponse(path,content_type='text/html',charset='utf-8')
#     # return HttpResponse('THIS IS VIEWS')

#     msg = HttpResponse(
#             ''' 
#             <br>
#             <br>Path : {path}
#             <br>Scheme : {scheme}
#             <br>Method : {method}
#             '''
#                        )
#     return msg

def home(request):
    return render(request, 'home.html')

def viewform(request):
    return render(request, 'form.html')

def form2(request):

    form = BookingForm()
    context = {"form":form}
    return render(request, "form.html",context)
   

def pathview(request, name, id): 

    htmlformat = HttpResponse("Name:{} <br> UserID:{}".format(name, id)) 
    return htmlformat

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def Relation(request, name):
    ddict = {'sagar': 'This is me', 'Anuj': 'this is my frnd 1', 'Shree': 'this is my frnd 2'}
    
    if name in ddict:
        htmlFT = HttpResponse(f"Name = {name} Relation = {ddict[name]}")
    else:
        htmlFT = HttpResponse(f"Name = {name} Relation = Not found")
    
    return htmlFT

# def myview(request): 
#     return HttpResponsePermanentRedirect(reverse('demoapp:login'))