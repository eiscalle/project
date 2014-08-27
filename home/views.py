# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from coffin.views.generic import TemplateView, CreateView, ListView
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils import translation
from django.utils.http import is_safe_url
from django.utils.translation import ugettext_lazy as _, check_for_language
from django.views.generic import RedirectView
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


def change_language(request, lang_code):
    next = request.REQUEST.get('next')
    if not is_safe_url(url=next, host=request.get_host()):
        next = request.META.get('HTTP_REFERER')
        if not is_safe_url(url=next, host=request.get_host()):
            next = '/'
    current_lang = request.LANGUAGE_CODE
    response = HttpResponseRedirect(next)
    if check_for_language(lang_code):
        response = HttpResponseRedirect(next.replace('/%s/' % current_lang, '/%s/' % lang_code))

        if hasattr(request, 'session'):
            request.session['django_language'] = lang_code
        else:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        translation.activate(lang_code)
    return response