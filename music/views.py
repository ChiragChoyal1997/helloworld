from django.shortcuts import render
from django.http import HttpResponse
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
    return HttpResponse("<h2>Details of album id = "+str(album_id)+"<h2>")