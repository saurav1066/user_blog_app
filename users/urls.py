from django.urls import path

from users.views import Register, HomePageView

urlpatterns = [
    path('signup/', Register.as_view())
]