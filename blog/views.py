from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.filter(last_modified__lte=timezone.now()).order_by('last_modified')
    return render(request, 'blog/post_list.html', {'posts': posts})

