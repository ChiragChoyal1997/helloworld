
import json
from django.http import Http404
from .models import Album
from django.shortcuts import render

# Create your views here.

def index(request):
    all_album = Album.objects.all()
    context = {
        "all_albums": all_album,
    }
    return render(request, 'music/index.html', context)

def details(request,album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except:
        raise Http404("Album does not exist")
    return render(request, "music/details.html", {'album': album})
