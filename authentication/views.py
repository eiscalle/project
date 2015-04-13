# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView

from authentication.forms import RegistrationForm
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


class LoginView(TemplateView):
    template_name = 'login.html'
    http_method_names = ['get', 'post']
    error = None

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        remember_me = request.POST.get('remember_me', None)

        auth_user = authenticate(username=username, password=password)
        if auth_user:
            login(request, auth_user)

            if not remember_me:
                request.session.set_expiry(0)
        else:
            self.error = _('Имя пользователя или пароль введены неверно.')
            return self.get(request, *args, **kwargs)

        if request.GET.get('next', ''):
            redirect_to = request.GET.get('next', '')
        else:
            redirect_to = '/'

        redirect_to = redirect_to if redirect_to else '/'
        return HttpResponseRedirect(redirect_to)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['error'] = self.error
        return context


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))