from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone

# Create your views here.

def main(request):
    blogs = Blog.objects.all() #쿼리셋 = 모델안의 오브젝트의 목록을 가져온다고 생각(list), 메소드

    return render(request, 'main.html', {'blogs' : blogs}) #'blogs'라는 키값으로 blog를 가져옴


def detail(request,blog_id):
    details=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'details':details})

def write(request):
    return render(request,'write.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('main')

def edit(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'blog':blog})

def update(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('main')

def delete(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    blog.delete()
    return redirect('main')


