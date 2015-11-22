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
    ).order_by('show_time')[:3]

    singers_list = Attachment.objects.filter(
        group='team'
    ).order_by('?')

    photo_list = Attachment.objects.filter(
        group="photo"
    ).order_by('?')

    context = {
        'concert_list': concert_list,
        'singers_list': singers_list,
        'photo_list': photo_list,
        'concert_item_width': int(100.0 / len(concert_list) - 5)
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

        print result

        return json.dumps({
            'result': result
        })

    raise Http404
