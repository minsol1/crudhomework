from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Blog
# Create your views here.
def home(request):
    blog = Blog.objects.all() #Blog에서 객체들을 모두 불러와서 blog에 저장
    return render(request, 'home.html', {'blog':blog})

def detail(request, id): #id는 각 객체의 아이디. urls.py에서 넘어온다.
	blog = get_object_or_404(Blog, pk = id)
	return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request,'new.html')

def create(request):
    newBlog = Blog()
    newBlog.title=request.POST['title']
    newBlog.writer=request.POST['writer']
    newBlog.body=request.POST['body']
    newBlog.pub_date=timezone.now()
    newBlog.save()
    return redirect('detail',newBlog.id)

def edit(request,id):
    blog=Blog.objects.get(id=id)
    return render(request,'edit.html',{'blog':blog})

def update(request,id):
    blog=Blog.objects.get(id=id)
    blog.title=request.POST['title']
    blog.writer=request.POST['writer']
    blog.body=request.POST['body']
    blog.pub_date=timezone.now()
    blog.save()
    return redirect('detail',blog.id)

def delete(request,id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    return redirect('home')
