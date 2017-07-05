from django.shortcuts import render
from django.views import generic
from .models import Year

class IndexView(generic.ListView):
    template_name = 'weeklist/index.html'

    def get_queryset(self):
        return Year.objects.all()


