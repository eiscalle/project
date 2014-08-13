# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from coffin.views.generic import ListView, CreateView
from django.utils.translation import ugettext_lazy as _
from series.forms import EpisodeCreateForm
from series.models import Episode


class EpisodeList(ListView):
    model = Episode
    template_name = 'episode_list.html'

    def get_queryset(self):
        return super(EpisodeList, self).get_queryset().filter(series_id=self.kwargs['series_id'])


class EpisodeCreate(CreateView):
    model = Episode
    form_class = EpisodeCreateForm
    template_name = 'episode_create.html'