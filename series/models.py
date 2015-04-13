# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.core.urlresolvers import reverse

from django.db import models
from django.utils.translation import ugettext_lazy as _

from authentication.models import User
from settings.constants import LANGUAGES


class Tag(models.Model):
    name = models.CharField(_('Название'), default='', max_length=255)

    class Meta:
        verbose_name = _('Тег')
        verbose_name_plural = _('Теги')

    def __unicode__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(_('Название'), default='', max_length=255, db_index=True)
    description = models.TextField(_('Описание'), default='', max_length=3000)
    original_language = models.CharField(_('Язык сериала'), max_length=24, choices=LANGUAGES,
                                         default=LANGUAGES[0][0])
    tags = models.ManyToManyField(Tag, verbose_name=_('Теги'), related_name='series', default=None,
                                  blank=True)

    def get_absolute_url(self):
        return reverse('episode_list', args=[self.pk])

    class Meta:
        verbose_name = _('Сериал')
        verbose_name_plural = _('Сериалы')

    def __unicode__(self):
        return self.name


class Episode(models.Model):
    name = models.CharField(_('Название'), default='', max_length=255)
    season = models.PositiveSmallIntegerField(_('Сезон'), default=1)
    number = models.PositiveSmallIntegerField(_('Номер серии'), default=1)
    source = models.CharField(_('Видеофайл'), max_length=255, default='')
    preview = models.CharField(_('Превью'), max_length=255, default='')
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    is_published = models.BooleanField(_('Опубликовано'), default=False)

    series = models.ForeignKey(Series, verbose_name=_('Сериал'), related_name='episodes')
    created_by = models.ForeignKey(User, verbose_name=_('Пользователь'), related_name='episodes')
    tags = models.ManyToManyField(Tag, verbose_name=_('Теги'), related_name='episodes', default=None,
                                  blank=True)

    class Meta:
        verbose_name = _('Серия')
        verbose_name_plural = _('Серии')

    def __unicode__(self):
        return '%s: %s' % (self.series.name, self.name)

    def get_absolute_url(self):
        return reverse('episode_detail', args=[self.series.pk, self.pk])

    # def get_upload_to(self):
    #     return 'series/%s/season_%s/'