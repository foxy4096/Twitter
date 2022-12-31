from django.shortcuts import render

from apps.tweet.models import Tweet
from apps.tweet.forms import TweetCreationForm


def frontpage(request):
    tweets = Tweet.objects.all()
    form = TweetCreationForm()
    return render(request, "core/frontpage.html", {"tweets": tweets, "form": form})
