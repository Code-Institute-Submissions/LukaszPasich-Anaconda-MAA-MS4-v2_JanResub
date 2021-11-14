from django.shortcuts import render
from .models import Class

# Create your views here.


def about(request):
    """ About page view """

    return render(request, 'classes/about.html')


def times(request):
    """ Times page view """

    return render(request, 'classes/times.html')


def all_classes(request):
    """ A view to show all classes"""

    classes = Class.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'classes/times.html', context)
