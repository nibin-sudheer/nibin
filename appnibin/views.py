from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nibin(request):
    return HttpResponse('Welcome Home')


def index(request):
    return render(request, 'index.html')


def index1(request):
    return render(request, 'index1.html')



