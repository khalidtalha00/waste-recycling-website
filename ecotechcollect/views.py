from django.http import HttpResponse
from django.shortcuts import render,redirect
from ecotechcollect.models import Feedback
def index(request):
    return render(request,'index.html')
def pickup(request):
    return render(request,'requestpickup.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def savefeedback(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        data=Feedback(name=name,email=email,message=message)
        data.save()
    return render(request,'savefeedback.html')





