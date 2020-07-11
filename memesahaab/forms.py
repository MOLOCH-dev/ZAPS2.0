from django import forms
from .models import Catg_Meme, Loss_Meme, Surreal_Meme, MemeMan_Meme

class MemeForm(forms.ModelForm):
    class Meta:
        model = Catg_Meme
        fields = ('title', 'author','caption', 'catg_meme', 'meme_file')

class LossForm(forms.ModelForm):
    class Meta:
        model = Loss_Meme
        fields = ('title', 'author','caption', 'loss_meme', 'loss_meme_comments')

class SurrealForm(forms.ModelForm):
    class Meta:
        model = Surreal_Meme
        fields = ('title', 'author','caption', 'surreal_meme', 'surreal_meme_comments')

class MememanForm(forms.ModelForm):
    class Meta:
        model = MemeMan_Meme
        fields = ('title', 'author','caption', 'mememan_meme', 'mememan_meme_comments')
