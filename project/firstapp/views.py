from django.shortcuts import render


# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request,'home.html')

def profile(request):
    return render(request,'profile.html')

def main(request):
    return render(request, 'main.html')




