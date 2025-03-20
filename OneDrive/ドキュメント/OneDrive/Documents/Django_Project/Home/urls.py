from django.urls import path
from Home import views

urlpatterns = [
    path('Home/', views.home, name='home'),
    path('form/',views.viewform,name='form'),
    path('form2/',views.form2,name='form2'),
    path('getuser/<str:name>/<int:id>', views.pathview, name='pathview'), 
    path('getuser/', views.qryview, name='qryview'),
    # path("showform/", views.showform, name="showform"),
    path("getform/", views.getform, name='getform'), 
    path('relation/<str:name>', views.Relation, name='Relation'), 
]


# #demoapp/urls.py 
# from django.urls import path 
# from . import views 

# app_name =  'Home'
# urlpatterns = [ 
#     path('', views.index, name='index'), 
#     path('login/', views.login, name='login') 
# ] 
