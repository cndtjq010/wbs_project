from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'blog/index.html')

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'blog/blog.html', {'postlist':postlist})

def posting(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'blog/new_post.html')
