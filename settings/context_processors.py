# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from series.models import Series


def series_list(request):
    return {'series_list': Series.objects.all()}