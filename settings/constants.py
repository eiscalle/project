# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('en', _('Английский')),
    ('ru', _('Русский')),
    ('ch', _('Китайский')),
)

LANGUAGE_CODES = [x[0] for x in LANGUAGES]
LANGUAGE_PATHS = ['/%s/' % x for x in LANGUAGE_CODES]