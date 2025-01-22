from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tweet_list/", views.tweet_list, name="tweet_list"),
    path("create/", views.tweet_create, name="tweet_create"),
    path("edit/<int:tweet_id>/", views.tweet_edit, name="tweet_edit"),
    path("delete/<int:tweet_id>/", views.tweet_delete, name="tweet_delete"),
    path("register/", views.register, name="register"),
    path("my_tweet/", views.my_tweet, name="my_tweet"),
    path("search/", views.search, name="search"),
]
