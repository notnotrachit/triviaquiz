from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request,'base.html',{"content": "Hello World!"})

def play(request):
    return render(request,'base.html',{"content":"Question"})
