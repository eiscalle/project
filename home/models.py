# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from settings.constants import LANGUAGES


class Feedback(models.Model):
    subject = models.CharField(_('Заголовок'), default='', max_length=255)
    message = models.TextField(_('Сообщение'), default='', max_length=2000)
    email = models.EmailField(_('E-mail'), default='', max_length=255)
    created_at = models.DateTimeField(_('Дата создания'), default=datetime.datetime.now(), auto_now_add=True)

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

    def __unicode__(self):
        return self.subject


class WantedSeries(models.Model):
    name = models.CharField(_('Название сериала'), default='', max_length=255)
    season = models.PositiveSmallIntegerField(_('Номер сезона'), default=1)
    language = models.CharField(_('Язык перевода'), choices=LANGUAGES, default=LANGUAGES[0][0], max_length=24)
    email = models.EmailField(_('E-mail'), default='', max_length=255)

    class Meta:
        verbose_name = _('Заказ сериала')
        verbose_name_plural = _('Заказы сериалов')

    def __unicode__(self):
        return self.name