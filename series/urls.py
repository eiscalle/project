from django.conf.urls import patterns, url
from django.contrib import admin

from series.views import EpisodeList, EpisodeCreate


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^(?P<series_id>\d+)/list/$', EpisodeList.as_view(), name='episode_list'),
    url(r'^create/$', EpisodeCreate.as_view(), name='episode_create'),
)
