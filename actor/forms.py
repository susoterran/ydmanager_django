from django.forms import inlineformset_factory
from actor.models import Actor
from django import forms

'''
ActorInlineFormSet = inlineformset_factory(Actor,
    fields = ['actor', 'image', 'title', 'description'],
    extra = 2)
'''
class ActorSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')