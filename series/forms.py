# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django import forms
from auth.models import User
from series.models import Episode


class RegistrationForm(forms.Form):
    username = forms.CharField(label=_('Имя пользователя'), max_length=64)
    email = forms.EmailField(label=_('E-mail адрес'), max_length=64, required=True)

    password = forms.CharField(label=_('Пароль'), max_length=64, required=True, widget=forms.PasswordInput, min_length=5)
    confirm_password = forms.CharField(label=_('Подтверждение пароля'), max_length=64, required=True,
                                       widget=forms.PasswordInput, min_length=5)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if not email:
            raise forms.ValidationError(_('Введите E-mail адрес.'))

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError(_('Пользователь с таким E-mail адресом уже существует.'))


    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if not username:
            raise forms.ValidationError(_('Введите имя пользователя.'))

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise forms.ValidationError(_('Пользователь с таким именем уже существует.'))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password', '')
        confirm_password = self.cleaned_data.get('confirm_password', '')

        if password != confirm_password:
            raise forms.ValidationError(_('Введенные пароли не совпадают.'))

        return confirm_password


class EpisodeCreateForm(forms.ModelForm):

    class Meta:
        model = Episode
        exclude = ('created_by', 'is_published')