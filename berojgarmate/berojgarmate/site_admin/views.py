from django.shortcuts import render
from client_jg.models import *

# Create your views here.

def index_page(request):
    return render(request, 'home_index/html/index.html')

def admin_signin(request):
    return render(request,'site_admin/html/admin_signin.html')

def admin_index(request):
    return render(request,'site_admin/html/admin_index.html')

def admin_signup(request):
    return render(request,'site_admin/html/admin_signup.html')



#
# def view_job(request):
#     crse=job_giver_details.objects.all()
#     return render(request,'app1/adminpages/veiwcourseadmin.html',{'crse':crse})