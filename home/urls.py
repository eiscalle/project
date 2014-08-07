from django.conf.urls import patterns, url
from django.contrib import admin

from home.views import HomePage


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', HomePage.as_view(), name='home'),
)
