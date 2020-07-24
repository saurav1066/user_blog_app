from django.urls import path

from users.views import Register

urlpatterns = [
    path('signup/', Register.as_view())
]