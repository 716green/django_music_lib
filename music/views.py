from django.shortcuts import render
from .models import Music

# Create your views here.
def index(request):
  return render(request, 'music.html', { 'hello': 'world' })
  
  
def detail(request, music_id):
  music = Music.objects.get(pk=music_id)
  return render(request, 'detail.html', { 'music': music})