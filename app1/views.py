from django.shortcuts import render

# Create your views here.
def poo(request):
    return render(request,'poo.html')