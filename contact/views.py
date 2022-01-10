from django.shortcuts import render

# Create your views here.


def contact(request):
    """ Contact page view """

    return render(request, 'contact/contact.html')

