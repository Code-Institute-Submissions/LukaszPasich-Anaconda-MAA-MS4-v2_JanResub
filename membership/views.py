from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
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
    if request.method == "POST":
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added membership!')
            return redirect(reverse('add_membership'))
        else:
            messages.error(request, '''Failed to add membership.
                                       Please ensure the form is valid''')
    else:
        form = MembershipForm()

    template = 'memberships/add_membership.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_membership(request, membership_id):
    """ A view to edit existing memberships"""
    membership = get_object_or_404(Membership, pk=membership_id)
    if request.method == "POST":
        form = MembershipForm(request.POST, instance=membership)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated membership!')
            return redirect(reverse('memberships'))
        else:
            messages.error(request, '''Failed to update product.
                           Please ensure the form is valid.''')
    else:
        form = MembershipForm(instance=membership)
        messages.info(request, f'''You are editing the membership:
                      {membership.name}''')

    template = 'memberships/edit_membership.html'
    context = {
        'form': form,
        'membership': membership,
    }

    return render(request, template, context)
