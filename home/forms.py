# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django import forms
from auth.models import User
from home.models import Feedback
from series.models import Episode


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = ('created_at', )