from django.shortcuts import render

def flash_cards(request):
    return render(request, "flashcards.html")
