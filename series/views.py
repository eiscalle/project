# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from coffin.views.generic import ListView, CreateView
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
from series.forms import EpisodeCreateForm
from series.models import Episode
from subtitles.forms import SubtitleFormset
from subtitles.models import Subtitle


class EpisodeList(ListView):
    model = Episode
    template_name = 'episode_list.html'

    def get_queryset(self):
        return super(EpisodeList, self).get_queryset().filter(series_id=self.kwargs['series_id'])


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
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        response = super(EpisodeCreate, self).form_valid(form)
        self.subtitle_formset.save()
        return response

    def get_context_data(self, **kwargs):
        context = super(EpisodeCreate, self).get_context_data(**kwargs)
        context['subtitle_formset'] = self.subtitle_formset
        return context
