from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
# # Create your views here.
#
# #
# # def home(request):
# #     # html_var = 'f string'
# #     # html_ = """<!DOCTYPE html>
# #     # <html lang=en>
# #     # <head> </head>
# #     # <body>
# #     # <h1> Hello World!</h1>
# #     # <p> This is {html_var} coming through</p>
# #     # </body>
# #     # </html>
# #     # """
# #     num = random.randint(0, 1000000)
# #     some_list = [num, random.randint(0, 1000000), random.randint(0, 1000000), random.randint(0, 1000000)]
# #     context = {
# #         'bool_item': False,
# #         'num': num,
# #         'some_list': some_list
# #     }
# #     return render(request, 'home.html', context)
# #     # return HttpResponse(html_)
# #
# #
# # def about(request):
# #     context = {}
# #     return render(request, 'about.html', context)
# #
# #
# # def contact(request):
# #     context = {}
# #     return render(request, 'contact.html', context)
# #
# #
# # class ContactView(View):
# #
# #     def get(self, request, *args, **kwargs):
# #         context = {}
# #         return render(request, 'contact.html', context)
#
#
# class HomeView(TemplateView):
#
#     template_name = 'home.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         print(context)
#         num = random.randint(0, 1000000)
#         some_list = [num, random.randint(0, 1000000), random.randint(0, 1000000), random.randint(0, 1000000)]
#         context = {
#             'bool_item': False,
#             'num': num,
#             'some_list': some_list
#         }
#         return context
#
#
# class AboutView(TemplateView):
#     template_name = 'about.html'
#
#
# class ContactView(TemplateView):
#
#     template_name = 'contact.html'

from .models import RestaurantLocation


# def restaurants_list_view(request):
#     template_name = 'restaurants/restaurantlocation_list.html'
#     query_set = RestaurantLocation.objects.all()
#     context = {
#         'object_list': query_set
#     }
#     return render(request, template_name, context)
#

class RestaurantListView(ListView):
    # template_name = 'restaurants/restaurantlocation_list.html'

    def get_queryset(self):
        # print(self.kwargs)
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
                )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    def get_context_data(self, *args, **kwargs):
        print(self.kwargs)
        context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestaurantLocation, id=rest_id)
        return obj

