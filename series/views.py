# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from coffin.views.generic import ListView, CreateView, DetailView
import datetime
from django.core.urlresolvers import reverse_lazy
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from series.forms import EpisodeCreateForm
from series.models import Episode, Series
from subtitles.forms import SubtitleFormset
from subtitles.models import Subtitle


class SeriesMixin(object):
    def get(self, request, *args, **kwargs):
        self.series = get_object_or_404(Series, pk=self.kwargs['series_id'])
        return super(SeriesMixin, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SeriesMixin, self).get_context_data(**kwargs)
        context['series'] = self.series
        return context


class EpisodeList(SeriesMixin, ListView):
    model = Episode
    template_name = 'episode_list.html'

    def get_queryset(self):
        return super(EpisodeList, self).get_queryset().filter(series_id=self.kwargs['series_id'])


class EpisodeDetail(SeriesMixin, DetailView):
    model = Episode
    template_name = 'episode_detail.html'


class EpisodeCreate(CreateView):
    model = Episode
    form_class = EpisodeCreateForm
    template_name = 'episode_create.html'

    def get(self, request, *args, **kwargs):
        self.subtitle_formset = SubtitleFormset()
        return super(EpisodeCreate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.form_class(request.POST, request.FILES)
        self.subtitle_formset = SubtitleFormset(request.POST, request.FILES)
        if form.is_valid() and self.subtitle_formset.is_valid():
            form.instance.created_by = request.user
            self.object = form.save()
            for form in self.subtitle_formset:
                form.instance.episode = self.object
                form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(EpisodeCreate, self).get_context_data(**kwargs)
        context['subtitle_formset'] = self.subtitle_formset
        return context