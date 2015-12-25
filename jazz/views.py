# coding: utf-8

import json

from datetime import datetime

from django.conf import settings
from django.shortcuts import render_to_response, HttpResponse
from django.template.context import RequestContext

from jazz.forms import FeedbackForm
from jazz.models import Concert, Attachment, Video


def index(request):
    concert_list = Concert.objects.filter(
        show_time__gte=datetime.today()
    ).order_by('show_time')[:3]

    singers_list = Attachment.objects.filter(group='team').order_by('?')
    photo_list = Attachment.objects.filter(group="photo").order_by('?')
    video_list = Video.objects.order_by('?')[:3]

    concert_item_width = None
    if concert_list:
        concert_item_width = int(100.0 / len(concert_list)) - 5,

    context = {
        'concert_list': concert_list,
        'singers_list': singers_list,
        'photo_list': photo_list,
        'video_list': video_list,
        'concert_item_width': concert_item_width,
        'phone_list': settings.PHONE_LIST
    }

    return render_to_response(
        'index.html', context, RequestContext(request)
    )


def feedback(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        form.save()
        response = {
            'response': 'OK'
        }
    else:
        response = {
            'response': 'Error',
            'error': form._errors
        }

    return HttpResponse(json.dumps(response))
