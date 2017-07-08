from django.shortcuts import render
from django.views import generic
from .models import Year, Week

class IndexView(generic.ListView):
    template_name = 'weeklist/index.html'

    def get_queryset(self):
        return Year.objects.all()


class DetailView(generic.DetailView):
    model = Year
    template_name = 'weeklist/detail.html'
