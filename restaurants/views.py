from django.shortcuts import render
from django.http import HttpResponse
import random
from django.views import View
from django.views.generic import TemplateView
# Create your views here.

#
# def home(request):
#     # html_var = 'f string'
#     # html_ = """<!DOCTYPE html>
#     # <html lang=en>
#     # <head> </head>
#     # <body>
#     # <h1> Hello World!</h1>
#     # <p> This is {html_var} coming through</p>
#     # </body>
#     # </html>
#     # """
#     num = random.randint(0, 1000000)
#     some_list = [num, random.randint(0, 1000000), random.randint(0, 1000000), random.randint(0, 1000000)]
#     context = {
#         'bool_item': False,
#         'num': num,
#         'some_list': some_list
#     }
#     return render(request, 'home.html', context)
#     # return HttpResponse(html_)
#
#
# def about(request):
#     context = {}
#     return render(request, 'about.html', context)
#
#
# def contact(request):
#     context = {}
#     return render(request, 'contact.html', context)
#
#
# class ContactView(View):
#
#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(request, 'contact.html', context)


class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        print(context)
        num = random.randint(0, 1000000)
        some_list = [num, random.randint(0, 1000000), random.randint(0, 1000000), random.randint(0, 1000000)]
        context = {
            'bool_item': False,
            'num': num,
            'some_list': some_list
        }
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):

    template_name = 'contact.html'
