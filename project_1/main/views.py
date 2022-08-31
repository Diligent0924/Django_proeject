from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def main(request):
    context ={
        "alert" : False
    }
    return render(request, 'main.html', context)