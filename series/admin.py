# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from series.models import Episode, Series, Tag
from subtitles.admin import SubtitleInline


class TagAdmin(admin.ModelAdmin):
    pass


class SeriesAdmin(admin.ModelAdmin):
    pass


class EpisodeAdmin(admin.ModelAdmin):
    inlines = [SubtitleInline, ]


admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Tag, TagAdmin)