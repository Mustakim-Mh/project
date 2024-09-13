import views 
from django.http import HttpResponse 
def AboutUs(request): 
 return HttpResponse("Welcome to My Project")
def ContactUs(request): 
 return HttpResponse("<h1>Md. Mustakim Hossain, \nMobile: 01303837816\nEmail: mustakimhossain987@gmail.com </h1>")

def ContactDetails(request, ContactId): 
 return HttpResponse(ContactId) 
from django.shortcuts import render 
def HomePage(request): 
 return render(request, "index.html") 
data={ 
'title':'Title: Home Page', 
'caption':'Welcome to My Project' 
} 