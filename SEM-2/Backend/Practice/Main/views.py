from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Room,Topic
from .form import RoomForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# def home(request):
#     return HttpResponse("This is the home page")
# def room(request):
#     return HttpResponse("This is room for chitchat")


# Room=[
#     {"No":1,"Title":"Common Room"},
#     {"No":2,"Title":"Doubt Room"},
#     {"No":3,"Title":"Discussion Room"},
# ]

# def home(request):
#     return render(request,'Home.html')

# def room(request):
#     context={"Data":Room}
#     return render(request,'Main/Room.html',context)

# def chat(request,roomno):
#     for i in Room:
#         if int(roomno)==i["No"]:
#             roomdata={"Page":i}
#             break
#     return render(request,"Main/Chat.html",roomdata)

def home(request):
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("pass")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    rooms = Room.objects.filter(
        Q(name__icontains=q) |
        Q(topic__name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    context = {
        "rooms": rooms,
        "topics": topics,
        "q": q
    }
    return render(request, "Home.html", context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def room(request):
    room=Room.objects.all()
    context={"Data":room}
    return render(request,'Main/Room.html',context)

@login_required(login_url='home')
def chat(request,roomno):
    roomdata=Room.objects.get(id=roomno)
    context={"Page":roomdata}
    return render(request,"Main/Chat.html",context)

@login_required(login_url='home')
def inform(request):
    Form=RoomForm()    
    if request.method=="POST":
        Form=RoomForm(request.POST)
        if Form.is_valid():
            Form.save()
            return redirect("Rooms") 
    context={"create":Form,"Topic":"Create Room"}
    return render(request,"Main/insertForm.html",context)

@login_required(login_url='home')
def upform(request,roomno):
    roomdata=Room.objects.get(id=roomno)
    Form=RoomForm(instance=roomdata)
    if request.user!=roomdata.host:
        return HttpResponse("You cannot edit")    
    if request.method=="POST":
        Form=RoomForm(request.POST,instance=roomdata)
        if Form.is_valid():
            Form.save()
            return redirect("Rooms") 
    context={"create":Form,"Topic":"Update Room"}
    return render(request,"Main/insertForm.html",context)

@login_required(login_url='home')
def delform(request, roomno):
    roomdata = Room.objects.get(id=roomno)
    if request.user!=roomdata.host:     
        return HttpResponse("You cannot edit")    
    if request.method == "POST":
        roomdata.delete()
        return redirect("Rooms")
    context = {"obj": roomdata}
    return render(request, "Main/delmess.html", context)