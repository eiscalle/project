# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from series.models import Episode
from settings.mixins import BootstrapFormMixin


class EpisodeCreateForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Episode
        exclude = ('created_by', 'is_published')