from pickle import FALSE
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post, Group
from .forms import PostForm


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
    aut = author__username=username
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Здесь код запроса к модели и создание словаря контекста
    context = {
        'posts': Post.objects.filter(author__username=username)[:10],
        'post_count' : Post.objects.filter(author__username=username).count(),
        'page_obj': page_obj,
        'user_post' : Post.objects.filter(author__username=username),
        'creator': aut
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


def post_create(request):
    error = ''
    if request.method == 'POST':
        Post.author = request.User
        if form.is_valid():
            Post.save()
            return redirect("index")
        else:
            error = 'Ошибка при заполнении'
    form = PostForm()
    data = {
        'form':form,
        'error': error
    }

    return render(request, 'posts/create_post.html/', data)
