from django.conf.urls import  url
from flashcards.views import prueba_nav
urlpatterns = [
    url(r'^$',prueba_nav,name = 'nav'),
]

