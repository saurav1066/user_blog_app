from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView,CreateView

from blog.forms import BlogCreation
from blog.models import Blog


class HomePage(TemplateView):
    template_name = 'index.html'


class BlogPage(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'obj'


class BlogPost(LoginRequiredMixin, CreateView):
    form_class = BlogCreation
    template_name = 'blog_form.html'
    success_url = '/blog'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

