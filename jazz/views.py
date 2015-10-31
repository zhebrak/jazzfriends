# coding: utf-8

import json

from datetime import datetime

from django.shortcuts import render_to_response, Http404
from django.template.context import RequestContext

from jazz.forms import FeedbackForm
from jazz.models import Concert, Attachment


def index(request):
    concert_list = Concert.objects.filter(
        show_time__gte=datetime.today()
    ).order_by('show_time')[:2]

    print concert_list

    choir_photo_list = Attachment.objects.filter(
        group='choir_photo'
    ).order_by('?')
    singers_photo_list = Attachment.objects.filter(
        group='singers_photo'
    ).order_by('?')

    context = {
        'concert_list': concert_list,
        'choir_photo_list': choir_photo_list,
        'singers_photo_list': singers_photo_list
    }

    return render_to_response(
        'index.html', context, RequestContext(request)
    )


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request)
        if form.is_valid():
            form.save()

            result = 'OK'
        else:
            result = 'Error'

        return json.dumps({
            'result': result
        })

    raise Http404
