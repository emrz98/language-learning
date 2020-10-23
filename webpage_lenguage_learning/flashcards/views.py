from django.shortcuts import render
from flashcards.models import FlashCard

def flash_cards(request,id = 0):
    flash = FlashCard.objects.all()
    context = {'flash':flash[0]}
    return render(request,"tab-flashcard/flashcards.html",context)

def audio_practice(request):
    return render(request,"audio-practice.html")

def prueba_nav(request):
    return render(request, "nav-bar.html")
