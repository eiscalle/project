from django.conf.urls import patterns, url
from django.contrib import admin

from home.views import HomePage
from video.views import VideoList


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^list/$', VideoList.as_view(), name='video_list'),
)
