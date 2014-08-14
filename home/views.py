# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from coffin.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from home.forms import FeedbackForm
from home.models import Feedback, WantedSeries


class HomePageView(TemplateView):
    template_name = 'home.html'


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('home')


class WantedSeriesView(CreateView):
    model = WantedSeries
    template_name = 'wanted_series.html'
    success_url = reverse_lazy('home')