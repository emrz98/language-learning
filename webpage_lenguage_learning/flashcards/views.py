from django.shortcuts import render
from flashcards.models import FlashCard
def flash_cards(request):
    
    flash = FlashCard.objects.all()
    context = {'flash':flash[0]}
    return render(request, "tab-flashcard/flashcards.html",context)

def prueba_nav(request):
    return render(request, "nav-bar.html")
