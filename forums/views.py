from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.contrib.auth.models import User
from .models import Forum
from .forms import ForumForm

# Create your views here.
def forums(request):
    """
    Renders a page showing all the forums
    """
    forums = Forum.objects.all()
    username = request.user.username
    return render(request, 'forums.html', {'forums': forums}, username)

def view_forum(request, id):
    """
    A view forum page with comments and also increments the views counter
    """
    forum = Forum.objects.get(id=id)

    # View Incrementer
    forumViews = get_object_or_404(Forum, pk=id)
    forumViews.views = F('views') + 1
    forumViews.save()

    user = request.user
    
    return render(request, 'view_forum.html', {'forum': forum, 'user': user})

def create_or_edit_forum(request, pk=None):
    """
    Create a  view that allows us to create
    or edit a forum post depending if the forum ID
    is null or not
    """
    forum = get_object_or_404(Forum, pk=pk) if pk else None
    username = request.user.username
    if request.method == 'POST':
        form = ForumForm(request.POST, instance=forum)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.author = username.capitalize()
            forum.save()
            return redirect(view_forum, forum.pk)
    else:
        form = ForumForm(instance=forum)
    return render(request, 'forumform.html', {'form': form})

def forum_upvote(request, pk=None):
    """
    Upvote view for forum
    """
    forum = get_object_or_404(Forum, pk=pk) if pk else None
    user = User.objects.get(email=request.user.email)
    forum.upvotes = F('upvotes') + 1
    forum.views = F('views') - 1
    user.profile.forum_upvotes += 1
    user.profile.save()
    forum.save()
    return redirect(view_forum, forum.pk)