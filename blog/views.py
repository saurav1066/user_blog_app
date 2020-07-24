from django.shortcuts import render




# class home_page(request):
#     context = {
#         'name': 'Saurav Adhikari'
#     }
#     return render(request, 'index.html', context)
from django.views.generic import TemplateView, ListView

from blog.models import Blog


class HomePage(TemplateView):
    template_name = 'index.html'


class BlogPage(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'obj'
# def blog_page(request):
#     obj = Blog.objects.all()
#     context = {
#         'object' : obj
#     }
#     return render(request, 'blog.html', context)
