from django.shortcuts import render
from django.http import HttpResponse


def room(request):
    context={
    # control settings for our hardware
    }
    return render(request,'user/room.html',context)

def billing(request):
    return render(request,'user/billing.html',{'title':'biling'})

#can add more views like roomservice, etc later
