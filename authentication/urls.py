from django.conf.urls import url
from django.contrib import admin
from authentication.views import LoginView, RegistrationView, logout_user

admin.autodiscover()


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    url(r'^logout/$', logout_user, name='logout'),
]
