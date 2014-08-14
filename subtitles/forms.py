# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms.models import inlineformset_factory
from auth.models import User
from django.utils.translation import ugettext_lazy as _
from series.models import Episode
from subtitles.models import Subtitle


SubtitleFormset = inlineformset_factory(Episode, Subtitle, extra=2, max_num=2, can_delete=False)