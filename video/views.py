# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView
from video.models import Video


class VideoList(ListView):
    model = Video
    template_name = 'video_list.html'