from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('index')


def say_hello(request):
    return HttpResponse('hello')


hello_world_context = {
    'name': False,
    'foo': 'world',
    'spam': 'spam'
}


def say_hello_world(request):
    return render(request, 'hello.html', hello_world_context)