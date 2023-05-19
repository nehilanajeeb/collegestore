from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from .views import *

urlpatterns =[
    path('home', home,name='home'),
    path('',views.index,name='index'),
    path('dept',dept,name='dept'),
    path('addform',views.addform,name='addform'),
    path('new',views.new,name='new'),
    path('login/', loginPage,name='login'),
    path('viewcart/', viewcart,name='viewcart'),
    path('addbook/', addbook,name='addbook'),
    path('register/', registerPage,name='register'),
    path('logout/', logoutPage,name='logout'),
    path('addtocart/<str:pk>', addtocart,name='addtocart'),
]