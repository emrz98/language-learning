from flashcards.models import FlashCard
from django import forms

class FormCard(forms.ModelForm):
    class Meta:
        model = FlashCard
        fields = ['anverso','reverso']