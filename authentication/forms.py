# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from authentication.models import User
from settings.mixins import CrispyFormMixin


class RegistrationForm(CrispyFormMixin, forms.ModelForm):
    username = forms.CharField(label=_('Имя пользователя'), max_length=30)
    email = forms.EmailField(label=_('Адрес электронной почты'), max_length=64, required=True)
    password = forms.CharField(label=_('Пароль'), max_length=128, required=True,
                                       widget=forms.PasswordInput, min_length=5)
    confirm_password = forms.CharField(label=_('Подтверждение пароля'), max_length=128, required=True,
                                       widget=forms.PasswordInput, min_length=5)

    form_action = 'registration'

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return
        raise ValidationError(_('Пользователь с таким адресом электронной почты уже существует.'), code='invalid_email')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password', '')
        confirm_password = cleaned_data.get('confirm_password', '')

        if password != confirm_password:
            raise forms.ValidationError(_('Введенные пароли не совпадают.'), code='invalid_passwords')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(CrispyFormMixin, forms.Form):
    username = forms.CharField(label=_('Имя пользователя'), max_length=30)
    password = forms.CharField(label=_('Пароль'), max_length=128, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(), label=_('Запомнить'), initial=True)

    form_action = 'login'

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        auth_user = authenticate(username=cleaned_data.get('username'), password=cleaned_data.get('password'))
        if not auth_user:
            raise ValidationError(_('Имя пользователя и/или пароль введены неверно.'), code='invalid')
        self.auth_user = auth_user
