from django.conf.urls import url

from . import views

app_name = 'weeklist'
urlpatterns = [
    # index page
    url(r'^$', views.IndexView.as_view(), name='index'),
    # weeklist/5
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #weeklist/week/5
    url(r'^(?P<var1>[0-9]+)/(?P<var2>[0-9]+)/$', views.SingleWeek, name='singleweek'),
]
