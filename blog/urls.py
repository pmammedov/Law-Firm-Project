from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',BlogListView.as_view(),name="index"),
    path('<int:pk>/<str:slug>/',postDetails.as_view(template_name='blog/details.html' ),name="post-details"),
    path('search/query/',SearchProduct.as_view(),name="search"),
    # path('add/',AddPostScreen.as_view(),name="add-post"),
]