from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',BlogListView.as_view(),name="index"),
    path('<int:pk>/<str:slug>/',postDetails.as_view(template_name='blog/details.html' ),name="post-details"),
    path('search/query/',SearchProduct.as_view(),name="search"),
    path('blog/',BackBlogListView.as_view(),name="blog_list"),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('article/',ArticleList.as_view(),name="list"),
    path('create_article/', CreateArticleView.as_view(), name="create_article"),
    path('article/<int:pk>/', ArticleDeleteView.as_view(), name='delete_blog'),
    
    

    

    
    # path('add/',AddPostScreen.as_view(),name="add-post"),
]