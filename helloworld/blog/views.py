from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .models import Post
from .forms import PostForm


def show_post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'show_post.html', {
        'entry': post,
    })


def create_post(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            return redirect(
                reverse('blogs:show_post', kwargs={'pk': new_post.pk})
            )
    return render(request, 'create_post.html', {
        'form': form,
    })
