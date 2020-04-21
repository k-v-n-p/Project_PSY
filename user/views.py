from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author':'KVNP',
        'title':'1st post',
        'content':'First post content',
        'date_posted':'18 april,2020'
    },
    {
        'author':'KVNP',
        'title':'2nd post',
        'content':'second post content',
        'date_posted':'18 april,2020'
    },

]


def room(request):
    context={
    #'posts': posts
    }
    return render(request,'user/room.html',context)

def billing(request):
    return render(request,'user/billing.html',{'title':'biling'})

