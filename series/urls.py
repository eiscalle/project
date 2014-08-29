from ajaxuploader.views import AjaxFileUploader
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from series.views import EpisodeList, EpisodeCreate, EpisodeDetail


urlpatterns = patterns(
    '',
    url(r'^(?P<series_id>\d+)/list/$', EpisodeList.as_view(), name='episode_list'),
    url(r'^(?P<series_id>\d+)/detail/(?P<pk>\d+)/$', EpisodeDetail.as_view(), name='episode_detail'),
    url(r'^create/$', login_required(EpisodeCreate.as_view()), name='episode_create'),
    url(r'^upload/$', login_required(AjaxFileUploader()), name='episode_upload'),
)
