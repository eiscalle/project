from django.conf.urls import patterns, url
from django.contrib import admin
from auth.views import LoginView, RegistrationView

from home.views import HomePage
from video.views import VideoList


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    url(r'^logout/$', 'auth.views.logout_user', name='logout'),

)
