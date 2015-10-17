from django.shortcuts import render_to_response
from django.template.context import RequestContext


def index(request):
    print '12312'
    return render_to_response(
        'index.html', {}, RequestContext(request)
    )
