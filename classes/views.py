from django.shortcuts import render

# Create your views here.


def about(request):
    """ About page view """

    return render(request, 'classes/about.html')
