from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):
    v1=int(request.POST['n1'])
    v2 = int(request.POST['n2'])
    return render(request,'result.html',{'r':v1+v2})