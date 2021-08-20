from django.forms import inlineformset_factory
from actor.models import Actor
from django import forms

class LabelSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')