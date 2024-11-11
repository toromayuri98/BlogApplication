from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from django.urls import reverse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def sign_up(request):
    form = RegisterForm()  
    if request.method == 'POST':
        form = RegisterForm(request.POST)  
        if form.is_valid():
            form.save()  
            return redirect('login')  
    return render(request, 'sign_up.html', {'form': form})


def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'home.html', {'posts' : posts, "user" : request.user})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('post-detail', kwargs={'id': post.author_id}))
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form, 'user' : request.user})


def post_detail(request, id): 
    post = Post.objects.filter(author_id = id).order_by('-date_posted').values()
    return render(request, 'post_details.html', {'posts': post})

def edit_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('post-detail', pk=post.pk)  

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('post-detail', kwargs={'id': post.author_id}))
    else:
        form = PostForm(instance=post)  
    return render(request, 'post_form.html', {'form': form, 'post': post})

def delete_post(request, id):
    post = get_object_or_404(Post, id=id) 
    post_to_delete = Post.objects.get(id = post.id).delete()
    return redirect(reverse('post-detail', kwargs={'id': post.author_id}))
     