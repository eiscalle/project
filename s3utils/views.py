# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload_success(request):
    filename = request.POST.get('key', '')
    return make_response(200, {'filepath': filename})


def make_response(status=200, content=None):
    if content is None:
        content = {}
    response = HttpResponse()
    response.status_code = status
    response['Content-Type'] = "application/json"
    response.content = json.dumps(content)
    return response