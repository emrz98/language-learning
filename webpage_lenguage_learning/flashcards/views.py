from django.shortcuts import render
from flashcards.models import FlashCard
import json

def flash_cards(request):
    flash = FlashCard.objects.all()
    #CARDS CON LISTAS 
    # cards = [[card.anverse, card.reverse] for card in flash]
    # cards = json.dumps(cards)

    #CARDS CON DIC
    cards = {"anverso": [card.anverse for card in flash] , "reverso" : [card.reverse for card in flash]}
    cards = json.dumps(cards)
    print(cards)
    context = {'flash':cards}

    return render(request,"tab-flashcard/flashcards.html",context)

def audio_practice(request):
    return render(request,"audio-practice.html")

def prueba_nav(request):
    return render(request, "nav-bar.html")
