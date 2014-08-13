from django.contrib import admin
from series.models import Episode, Series, Tag


class SeriesAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


class EpisodeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Tag, TagAdmin)