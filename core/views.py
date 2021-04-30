from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome):
    return HttpResponse('<h1>Hello World!</h1>\n<h2>Hello {}</h2>'.format(nome))

def soma(request, a, b):
    soma = int(a) + int(b)
    return HttpResponse('<h1>Soma de {} e {} : {}</h1>'.format(a,b,soma))