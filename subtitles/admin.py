# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from subtitles.models import Subtitle


class SubtitleInline(admin.StackedInline):
    model = Subtitle
    extra = 2
