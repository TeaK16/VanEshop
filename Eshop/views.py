from base64 import b64encode
from django.shortcuts import render, redirect, get_object_or_404

from Eshop.models import Van
from .forms import VanForm, MakeReservationForm, RentVanForm
from django.contrib import messages

# Create your views here.
def vans(request):
    qs = Van.objects.all()
    context = {"vans":qs}
    return render(request, 'vans.html',context)

def contact(request):
    return render(request,'contact.html')


def vans_detail_view(request, id=None):
    van_obj = None
    if id is not None:
        van_obj = Van.objects.get(id=id)

    context = {
        "object": van_obj,
    }

    return render(request,"vans/detail.html",context)

def addvan(request):
    if request.method == "POST":

        if request.user.is_superuser:
            form = VanForm(request.POST, request.FILES)
           
        if form.is_valid():
            van = form.save(commit=False)
            van.user = request.user
            form.save()
            return redirect("vans")

    # if a GET (or any other method) we'll create a blank form
    else:
        if request.user.is_superuser:
            form = VanForm()

    context = {"form":form}
    return render(request,"vans/addvan.html",context)

def editvan(request,id):
    van_obj = get_object_or_404(Van, id = id)

    if request.method == 'GET':
        context = {"form":VanForm(instance=van_obj), 'id':id}
        return render(request,'vans/addvan.html', context)
    
    elif request.method == 'POST':
        if request.user.is_superuser:
            form_data = VanForm(request.POST, instance=van_obj)
        
        if form_data.is_valid():
            form_data.save()

            return redirect("vans")
        else:
            
            return render(request,"vans/addvan.html",{"form":form_data})


def deletevan(request,id):
    van_obj = get_object_or_404(Van, id = id)
    if request.user.is_superuser:
        van_obj.delete()
    return redirect("vans")

#---User action
def makereservation(request,id):
    van_obj = get_object_or_404(Van, id = id)

    if request.method == "POST":
        if not request.user.is_superuser:
            form = MakeReservationForm(request.POST, request.FILES)
        
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.van = van_obj
            form.save()
            return redirect("vans")
    # if a GET (or any other method) we'll create a blank form
    else:
        if not request.user.is_superuser:
            form = MakeReservationForm(instance=van_obj)

    context = {"form":form,'id':id}
    return render(request,"vans/form/makereservation.html", context)

def rent(request,id):
    van_obj = get_object_or_404(Van, id = id)

    if request.method == "POST":
        if not request.user.is_superuser:
            form = RentVanForm(request.POST, request.FILES)

        if form.is_valid():
            rent = form.save(commit=False)
            rent.user = request.user
            rent.van = van_obj
            form.save()
            return redirect("vans")
    else:
        if not request.user.is_superuser:
            form = RentVanForm(instance=van_obj)

    context = {"form":form, 'id':id}
    return render(request,"vans/form/rentvan.html", context)

