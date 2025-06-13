from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Comment

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-published_date')
    return render(request, 'blog/author_posts.html', {'author': author, 'posts': posts})