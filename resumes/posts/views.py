from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post, User


def paginator_get(queryset, request):
    paginator = Paginator(queryset, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return {
        'paginator': paginator,
        'page_number': page_number,
        'page_obj': page_obj,
    }


def index(request):
    template = 'posts/index.html'
    title = 'Главная страница'
    groups = Group.objects.all()
    context = {
        'title': title,
        'groups': groups,
    }
    return render(request, template, context)


def all_group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'title': group.title,
        'posts': posts,
    }
    context.update(paginator_get(group.posts.all(), request))
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile_list = Post.objects.filter(author=user)
    context = {
        'author': user,
        'profile_list': profile_list
    }
    context.update(paginator_get(user.posts.all(), request))
    return render(request, 'posts/profile.html', context)


def resume_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'posts/resume_detail.html', context)


@login_required
def resume_create(request):
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('posts:profile', request.user)
    else:
        form = PostForm()
        title = 'Новое резюме.'
        context = {
            'form': form,
            'title': title,
        }
        return render(request, 'posts/create_resume.html', context)
    return render(request, 'posts/create_resume.html')


@login_required
def resume_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(
            request.POST or None,
            files=request.FILES or None,
            instance=post
        )
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('posts:resume_detail', post_id=post.id)
    else:
        form = PostForm()
        context = {
            'form': form,
            'is_edit': True,
        }
    context = {'form': form}
    return render(request, 'posts/create_resume.html', context)


@login_required
def resume_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return render(request, 'posts/resume_delete.html')
