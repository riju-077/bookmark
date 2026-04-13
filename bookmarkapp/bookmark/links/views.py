from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Bookmark
from .forms import BookmarkForm


@login_required
def home(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'links/home.html', {'bookmarks': bookmarks})


@login_required
def create_bookmark(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = BookmarkForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.save()
            return redirect('home')
            # return HttpResponseRedirect("/thanks/")
 
    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookmarkForm()

    return render(request, 'links/create.html', {"form": form})


@login_required
def edit_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk, user=request.user)
    if request.method == "POST":
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'links/edit.html', {'form': form})


