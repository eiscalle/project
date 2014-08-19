# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from series.models import Episode
from settings.constants import LANGUAGES


class Subtitle(models.Model):
    source = models.FileField(_('Исходный файл'), upload_to='video/%Y/%m/%d/subs/', max_length=255)
    language = models.CharField(_('Язык'), max_length=24, choices=LANGUAGES, default=LANGUAGES[0][0])

    episode = models.ForeignKey(Episode, verbose_name=_('Сериал'), related_name='episodes')

    class Meta:
        verbose_name = _('Субтитр')
        verbose_name_plural = _('Субтитры')

    def __unicode__(self):
        return '%s' % (self.language)
