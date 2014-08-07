# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'