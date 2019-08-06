"""Instagram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sort_integers(request):
    """Hi."""
    numbers = sorted(list(map(int, request.GET['numbers'].split(','))))
    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Integers sorted successfully.'
    }
    # import pdb; pdb.set_trace()
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )


def say_hi(request, name, age):
    if age < 12:
        message = 'Hola {}. No puedes usar esta alicación pues tiene {} años.'.format(name, age)
    else:
        message = 'Hola {}. Esperamos disfrutes tu experiencia.'.format(name)

    return HttpResponse(message)
