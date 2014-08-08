# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from auth.models import User


class Tag(models.Model):
    name = models.CharField(_('Название'), default='', max_length=255)


class Video(models.Model):
    name = models.CharField(_('Название'), default='', max_length=255)
    source = models.FileField(_('Видеофайл'), upload_to='video/%Y/%m/%d')
    preview = models.ImageField(_('Превью'), upload_to='screensavers/%Y/%m/%d')
    created_by = models.ForeignKey(User, verbose_name=_('Пользователь'), related_name='videos')
    tags = models.ForeignKey(Tag, verbose_name=_('Теги'), related_name='videos')
    created_at = models.DateTimeField(_('Дата создания'), default=datetime.datetime.now(), auto_now_add=True)
    is_published = models.BooleanField(_('Опубликовано'), default=False)

    class Meta:
        verbose_name = _('Видео')
        verbose_name_plural = _('Видео')

    def __unicode__(self):
        return self.name
