from django.contrib import admin
from . import views
from django.urls import path

app_name = "polls"
urlpatterns = [
    path("",views.IndexView.as_view(), name='index'),
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    path("<int:pk>/result", views.ResultsView.as_view(), name='results'),
    path("<int:question_id>/vote", views.vote, name='vote'),

]