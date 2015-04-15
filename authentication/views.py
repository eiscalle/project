# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView

from authentication.forms import RegistrationForm, LoginForm
from authentication.models import User
from django.utils.translation import ugettext_lazy as _


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    request = None

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )

        auth_user = authenticate(username=user.username, password=form.cleaned_data['password'])
        login(self.request, auth_user)

        return HttpResponseRedirect(reverse('home'))


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    http_method_names = ['get', 'post']
    error = None

    def form_valid(self, form):
        login(self.request, form.auth_user)
        if not form.cleaned_data.get('remember_me', True):
            self.request.session.set_expiry(0)

        if self.request.GET.get('next', ''):
            redirect_to = self.request.GET.get('next', '')
        else:
            redirect_to = reverse('home')
        return HttpResponseRedirect(redirect_to)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))