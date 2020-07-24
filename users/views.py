from django.views.generic import CreateView, TemplateView

from users.forms import Registration_Form


class Register(CreateView):
    form_class = Registration_Form
    template_name = 'registration.html'
    success_url = "/login"


class HomePageView(TemplateView):
    template_name = 'home.html'
