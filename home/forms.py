# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django import forms
from authentication.models import User
from home.models import Feedback, WantedSeries
from series.models import Episode
from settings.mixins import BootstrapFormMixin


class FeedbackForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = ('created_at', )


class WantedSeriesForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = WantedSeries
        exclude = []