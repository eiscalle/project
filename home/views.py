# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from coffin.views.generic import TemplateView, CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from home.forms import FeedbackForm, WantedSeriesForm
from home.models import Feedback, WantedSeries
from series.models import Series


class HomePageView(TemplateView):
    template_name = 'home.html'


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('home')


class WantedSeriesView(CreateView):
    model = WantedSeries
    form_class = WantedSeriesForm
    template_name = 'wanted_series.html'
    success_url = reverse_lazy('home')


class SearchView(ListView):
    model = Series
    template_name = 'search.html'

    def get_queryset(self):
        qs = super(SearchView, self).get_queryset()
        if self.search:
            qs = qs.filter(name__icontains=self.search)
        return qs

    def get(self, request, *args, **kwargs):
        self.search = request.GET.get('search', None)
        return super(SearchView, self).get(request, *args, **kwargs)