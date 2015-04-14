# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms import HiddenInput

from series.models import Episode
from settings.mixins import CrispyFormMixin


class EpisodeCreateForm(CrispyFormMixin, forms.ModelForm):

    class Meta:
        model = Episode
        exclude = ('created_by', 'is_published')
        widgets = {
            'source': HiddenInput(),
            'preview': HiddenInput(),
        }