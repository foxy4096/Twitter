from django.urls import path
from . import views

app_name = "userprofile"
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("edit/", views.edit_profile, name="edit_profile"),
    path("<str:username>/", views.user_details, name="user_details"),    
]
