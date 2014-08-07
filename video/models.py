# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Video(models.Model):
    name = models.CharField(_('Название'), default='', max_length=255)
    source = models.FileField(_('Видеофайл'), upload_to='video/%Y/%m/%d')
    screensaver = models.ImageField(_('Скринсейвер'), upload_to='screensavers/%Y/%m/%d')

    class Meta:
        verbose_name = _('Видео')
        verbose_name_plural = _('Видео')
