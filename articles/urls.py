from django.contrib import admin
from django.urls import path

from .views import (
    ArticleListView, 
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
)


urlpatterns = [
    path('new/', ArticleCreateView.as_view(), name="article_new"),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_edit"),
    path('<int:pk>/detele/', ArticleDeleteView.as_view(), name="article_delete"),
    path('', ArticleListView.as_view(), name='article_list'),
]