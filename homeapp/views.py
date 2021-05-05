from django.shortcuts import render,HttpResponse
from homeapp.models import Contact
# Create your views here.
def home(request):
    return HttpResponse("this is the homepage")

def contact(request):
    if(request.method =="POST"):
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact = Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
    return render(request,'contact.html')