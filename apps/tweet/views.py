from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .forms import TweetCreationForm
from .models import Tweet


@login_required
def create_tweet(request: HttpRequest) -> HttpResponseRedirect:
    """
    Create a new tweet.

    Args:
        request: The request object.

    Returns:
        The response redirect object.
    """

    if request.method == "POST":
        form = TweetCreationForm(request.POST)
        if form.is_valid():
            tweet: Tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            messages.success(request, "Tweet created.")
            return redirect("frontpage")
    return redirect("frontpage")

@login_required
def delete_tweet(request: HttpRequest, tweet_id:int) -> HttpResponseRedirect:
    """
    Delete a tweet.
    
    Args:
        request: The request object.
        tweet_id: The id of Tweet:
    """            
    tweet: Tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    tweet.delete()
    return redirect("frontpage")
