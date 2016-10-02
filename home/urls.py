from django.conf.urls import url
from django.contrib import admin

from home.views import HomePageView, FeedbackView, WantedSeriesView, SearchView


admin.autodiscover()

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
    url(r'^wanted/$', WantedSeriesView.as_view(), name='wanted_series'),
    url(r'^search/$', SearchView.as_view(), name='search'),
]
