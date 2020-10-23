from django.contrib import admin
from flashcards import models
admin.site.register(models.User)
admin.site.register(models.FlashCard)
# Register your models here.
