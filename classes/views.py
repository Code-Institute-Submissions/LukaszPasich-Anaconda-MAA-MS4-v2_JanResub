from django.shortcuts import render
from .models import Class

# Create your views here.


def about(request):
    """ About page view """

    return render(request, 'classes/about.html')


def all_classes(request):
    """ A view to show all classes"""

    mon_classes = Class.objects.all()[:8]
    tue_classes = Class.objects.all()[8:16]

    context = {
        'mon_classes': mon_classes,
        'tue_classes': tue_classes,
    }

    return render(request, 'classes/times.html', context)
