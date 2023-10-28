from django.urls import path , include
from .import views
from django.contrib import admin
from django.urls import path , include
from django.contrib import admin



urlpatterns = [
    
    path('',views.index_page, name='index'),

    path('admin_signup/', views.admin_signup,name="admin_signup"),
    path('admin_signin/', views.admin_signin,name="admin_signin"),
    path('admin_index/', views.admin_index,name="admin_index"),



]
