from django.contrib import admin
from video.models import Video


class VideoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)