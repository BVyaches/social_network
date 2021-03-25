from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CreationForm
from .models import Post, Group


def index(request):
    latest = Post.objects.all()[:10]
    return render(request, 'index.html', {'posts': latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('pub_date')[:12]
    return render(request, 'group.html', {'group': group, 't': posts})



@login_required
def new_post(request):
    form = CreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect("index")
    return render(request, "new.html", {"form": form})
