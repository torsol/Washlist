from django.shortcuts import render
from django.views import generic
from .models import Year, Week
import datetime

class IndexView(generic.ListView):
    template_name = 'weeklist/index.html'

    def get_queryset(self):
        return Year.objects.all()


class DetailView(generic.DetailView):
    model = Year
    template_name = 'weeklist/detail.html'

    def get_week_num(self):
        dt = datetime.date.today()
        wk = dt.isocalendar()[1]
        return wk

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['current_week'] = self.get_week_num()
        return context
