from django.conf.urls import patterns, url
from django.contrib import admin
from authentication.views import LoginView, RegistrationView

from home.views import HomePageView
from series.views import EpisodeList


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    url(r'^logout/$', 'authentication.views.logout_user', name='logout'),

)
