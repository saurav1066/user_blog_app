from django.urls import path
from django.contrib.auth import views as auth

from blog.views import HomePage, BlogPage, BlogPost

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('blog/', BlogPage.as_view(), name='blog'),
    path('blog/create_blog/', BlogPost.as_view()),
]