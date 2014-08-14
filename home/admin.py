# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from home.models import Feedback, WantedSeries


class FeedbackAdmin(admin.ModelAdmin):
    pass


class WantedSeriesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(WantedSeries, WantedSeriesAdmin)