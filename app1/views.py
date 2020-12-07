from django.shortcuts import render,redirect
from app1.models import *

# Create your views here.

def homepage(request):
    count_of_admin = user.objects.all().count()
    print(count_of_admin)
    if(count_of_admin==0):
        return redirect('http://127.0.0.1:8000/signup')
    else:
        return redirect('http://127.0.0.1:8000/login')

def login1(request):
    if(request.method=="GET"):
        return render(request,'home.html')
    else:
        a = request.POST.get("user_password")
        b = request.POST.get("user_email")
        print(a,b)
        try:
            x = user.objects.get(email=b,password=a)
            print("hello")

            request.session["session_email" ]= b
            print("world")
            
            return redirect('http://127.0.0.1:8000/homepage')
        except:
            return render(request,'home.html')

def signup1(request):
    if(request.method=="GET"):
        return render(request,'signup.html')
    else:
        
        a = request.POST.get('user_emailid')
        b = request.POST.get('user_name')
        c = request.POST.get('user_password')
        user(name=b,email=a,password=c).save()
        return redirect('http://127.0.0.1:8000/signup')

    
def homepage1(request):
    try:
        a = request.session["session_email"]
        return render(request,'homepage.html')
    except:
        return redirect('http://127.0.0.1:8000/login')

def addmovie1(request):
    if(request.method=="GET"):  
        return render(request,'addmovie.html')
    else:
       
        name = request.POST.get("name")
        director = request.POST.get("director")
        duration = request.POST.get("duration")
        description = request.POST.get("description")
        print(name,director,description,duration)
        movie(movie_name=name,movie_description=description,movie_director=director,movie_duration=duration).save()
        return render(request,'addmovie.html',{"msg":"MOvie Added"})

def listofmovies1(request):
    ticket  = movie.objects.all()
    return render(request,'listofmovies.html',{"tickets":ticket})

def addtiming(request,id):
    movie_name = movie.objects.get(id=id)
    if(request.method=="GET"):
        return render(request,'addtiming.html',{"movie":movie_name})
    else:
        timing = request.POST.get("timing")
        price = request.POST.get("price")
        no_of_ticket = request.POST.get("no_of_ticket")
        ticket(ticket_of_movie=movie_name,price=price,timing=timing,no_of_ticket=no_of_ticket).save()
        return render(request,"addtiming.html",{"msg":"Timing added"})
        
def availableticket1(request):
    tickets =ticket.objects.all()
    return render(request,'availableticket.html',{"tickets":tickets})

def purchaseticket1(request,id):
    movie_ticket = ticket.objects.get(id =id)
    print(movie_ticket)
    x = movie_ticket.no_of_ticket-1
    movie_ticket.no_of_ticket= x
    movie_ticket.save()
    return redirect('http://127.0.0.1:8000/availableticket')

