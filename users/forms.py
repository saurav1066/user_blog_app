from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class Registration_Form(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('first_name','last_name', 'email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name','last_name', 'email',)