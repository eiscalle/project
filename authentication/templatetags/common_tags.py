# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re
from django.template import Library
from django.template.loader import render_to_string
from django.utils.encoding import force_unicode
from django.utils import timezone
from django.core.urlresolvers import reverse

import datetime
from settings.constants import LANGUAGE_PATHS

register = Library()


@register.filter('dict_value')
def dict_value(dictionary, key):
    if dictionary:
        return dictionary.get(key)
    else:
        return None

@register.simple_tag(takes_context=True)
def is_active_menu(context, view_name, *args, **kwargs):
    if view_name == 'home' and context.request.path not in LANGUAGE_PATHS:
        return ''
    url = reverse(view_name, args=args, kwargs=kwargs)
    if url in context.request.path:
        return "class='active'"
    return ''
