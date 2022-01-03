from django.shortcuts import render
from .models import Membership
from .forms import MembershipForm

# Create your views here.


def all_memberships(request):
    """ A view to show all memberships"""

    memberships = Membership.objects.all()

    context = {
        'memberships': memberships,
        'on_all_memberships_page': True,
    }

    return render(request, 'memberships/memberships.html', context)


def add_membership(request):
    """ A view to add new memberships"""

    form = MembershipForm()
    template = 'memberships/add_membership.html'
    context = {
        'form': form,
    }

    return render(request, template, context)