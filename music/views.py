from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    # instead of: try,except -> album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        select_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album':album,
            'error_message': "You did not select a valid song",
        })
    else:
        select_song.is_favorite = True
        select_song.save()
        return render(request, 'music/detail.html', {'album': album})