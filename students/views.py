from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from students.models import UserEnquiry

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def saveEnquiry(request):    #saveEnquiry function h!
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        city=request.POST.get('city')
        text=request.POST.get('text')
        
        en=UserEnquiry(fname=fname,lname=lname, phone=phone,email=email,city=city,text=text)
        en.save()
        return HttpResponseRedirect('/thank')
    return render(request,"contact.html")



def thank(request):
    return render(request,"thank.html")








def service(request):
    return render(request,"service.html")
