from django.shortcuts import render

def flash_cards(request):
    return render(request, "flashcards.html")

def prueba_nav(request):
    return render(request, "nav-bar.html")
