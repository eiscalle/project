from django.conf.urls import patterns, url
from django.contrib import admin

from home.views import HomePageView, FeedbackView, WantedSeriesView


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
    url(r'^wanted/$', WantedSeriesView.as_view(), name='wanted_series'),
)
