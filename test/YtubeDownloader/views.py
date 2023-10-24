from django.shortcuts import render, redirect
from django.http import HttpResponse
from pytube import YouTube
from requests import get
def home(request):
    if request.POST:
        url = request.POST.get('url')
        if 'tube' in url or 'youtu.be' in url:
            req = get(url)
            if req.status_code == 200:
                yt = YouTube(url).streams.get_by_itag(22).url
                return redirect(yt, permanent=True)
        else:
            err = {
                "err" : 'please enter a valid url'
                    }
            return render(request, 'index.html', err)

    return render(request, 'index.html')

def query(request, data):
    return redirect('home')
# Create your views here.
