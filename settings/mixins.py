# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from crispy_forms.layout import Submit
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper


class CrispyFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(CrispyFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))