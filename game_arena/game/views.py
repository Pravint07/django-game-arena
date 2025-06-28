from django.shortcuts import render

def index(request):
    return render(request, 'game/index.html')

def play_game(request):
    return render(request, 'game/play.html')
