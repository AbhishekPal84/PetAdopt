from django.shortcuts import render,redirect
from .models import Contact
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        c = Contact(name=name , email=email , phone=phone , message=message)
        c.save()
        return redirect('/contact')
    data = Contact.objects.all()
    return render(request, 'contact.html', {"data":data})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')