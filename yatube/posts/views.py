from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post, Group, User
from .forms import PostForm


COUNT_POSTS = 10

def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }

    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    post_list = Post.objects.filter(author__username=username).order_by('-pub_date')
    author = get_object_or_404(User, username=username)
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Здесь код запроса к модели и создание словаря контекста
    context = {
        'posts': Post.objects.filter(author__username=username)[:COUNT_POSTS],
        'post_count' : Post.objects.filter(author__username=username).count(),
        'page_obj': page_obj,
        'user_post' : Post.objects.filter(author__username=username),
        'author': author
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    post = Post.objects.get(pk=post_id)
    post_cnt = post.author.posts.count()
    context = {
        'post' : Post.objects.get(pk=post_id),
        'post_cnt' : post_cnt,
    }
    return render(request, 'posts/post_detail.html', context) 


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.author = request.user
        new_post.save()
        return redirect('posts:profile', username=request.user)
    context = {'form': form,
        }
    return render(request, 'posts/create_post.html', context)


@login_required
def post_edit(request, post_id):
    template = 'posts/create_post.html'
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        return redirect('posts:post_detail', post_id=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post_id)
    return render(request, template,
                  {'form': form,})
