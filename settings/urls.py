from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

from django.contrib import admin

from home.views import change_language

admin.autodiscover()

urlpatterns = [
    url(r'^', include('authentication.urls')),
    url(r'^ajax-uploader/', include('ajaxuploader.urls', namespace='ajaxuploader', app_name='ajaxuploader')),
    url(r'^s3utils/', include('s3utils.urls', namespace='s3utils', app_name='s3utils')),
    url(r'^change_lang/(?P<lang_code>(en|ru))/$', change_language, name='change_language'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    url(r'^series/', include('series.urls')),
    url(r'^', include('home.urls')),
)