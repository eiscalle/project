from django.conf.urls import url

from s3utils.views import upload_success

urlpatterns = [
    url(r'^success/$', upload_success, name='upload_success'),
]
