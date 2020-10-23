from django.conf.urls import  url
from flashcards.views import prueba_nav, audio_practice
urlpatterns_flashcards = [
    url(r'^flashcards/$',prueba_nav,name = 'nav'),
    url(r'^audio/$', audio_practice, name ='audio'),
]