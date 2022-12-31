from django.forms import ModelForm

from .models import Tweet

class TweetCreationForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['body']
    