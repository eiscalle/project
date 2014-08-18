from django.conf.urls import patterns, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from series.views import EpisodeList, EpisodeCreate


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^(?P<series_id>\d+)/list/$', EpisodeList.as_view(), name='episode_list'),
    url(r'^create/$', login_required(EpisodeCreate.as_view()), name='episode_create'),
)
