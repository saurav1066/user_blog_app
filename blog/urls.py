from django.urls import path

from blog.views import HomePage, BlogPage

urlpatterns = [
    path('', HomePage.as_view()),
    path('blog', BlogPage.as_view(), name='blog')
]