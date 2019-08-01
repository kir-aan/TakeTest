from django.shortcuts import render
from Test.models import TestInfo
def home(request):
    tests =  TestInfo.objects.all()
    return render(request, 'TakeTestApp/home.html',{'tests':tests})

def about(request):
    return render(request, 'TakeTestApp/about.html')
