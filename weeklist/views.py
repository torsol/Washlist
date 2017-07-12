from django.shortcuts import render, get_object_or_404
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
        context['start'] = self.get_week_num()-1
        return context

def SingleWeek(request, var1, var2):
    year = get_object_or_404(Year, id=var1)
    week = year.week_set.get(week_num=var2)

    return render(request, 'weeklist/singleweek.html', {'week': week, })