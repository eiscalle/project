# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _


class BootstrapFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(BootstrapFormMixin, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})