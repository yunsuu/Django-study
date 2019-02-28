from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog, Comments
from .form import BlogPost, CommentForm

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts= paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts }) 

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request): # new.html띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() 
    return redirect('/blog/'+str(blog.id))

def blogpost(request): # 새 글 쓰기 (form)
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')        
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})

def new_comment(request):
    if request.method =='POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.date = timezone.now()
            comment.save()
            return redirect('home')
    else:
        commentform = CommentForm()
        return render(request, 'comment.html', {'commentform':commentform})
