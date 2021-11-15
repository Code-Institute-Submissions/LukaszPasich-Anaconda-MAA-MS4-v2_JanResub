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
    wed_classes = Class.objects.all()[16:24]
    thu_classes = Class.objects.all()[24:32]
    fri_classes = Class.objects.all()[32:40]
    sat_classes = Class.objects.all()[40:48]

    context = {
        'mon_classes': mon_classes,
        'tue_classes': tue_classes,
        'wed_classes': wed_classes,
        'thu_classes': thu_classes,
        'fri_classes': fri_classes,
        'sat_classes': sat_classes,
    }

    return render(request, 'classes/times.html', context)
