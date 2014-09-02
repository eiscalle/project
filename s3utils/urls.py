from ajaxuploader.views import AjaxFileUploader
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from series.views import EpisodeList, EpisodeCreate, EpisodeDetail


urlpatterns = patterns(
    's3utils.views',
    url(r'^success/$', 'upload_success', name='upload_success'),
)
