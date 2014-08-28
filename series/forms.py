# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from series.models import Episode


class EpisodeCreateForm(forms.ModelForm):

    class Meta:
        model = Episode
        exclude = ('created_by', 'is_published')