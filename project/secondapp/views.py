from django.shortcuts import render, redirect
from .forms import Write
from .models import Blog


# Create your views here.


def contact(request):
    return render(request,'contact.html')


def write(request):
    if request.method == 'POST':
        
        form = Write(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            return redirect('home')
    else:
        form = Write()
        return render(request, 'write.html',{'form' : form})