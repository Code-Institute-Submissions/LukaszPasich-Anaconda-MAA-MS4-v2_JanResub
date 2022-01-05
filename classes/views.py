from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Class
from .forms import ClassForm

# Create your views here.


def about(request):
    """ About page view """

    return render(request, 'classes/about.html')


def all_classes(request):
    """ A view to show all classes"""

    classes = list(Class.objects.all())

    mon_classes = classes[:8]
    tue_classes = classes[8:16]
    wed_classes = classes[16:24]
    thu_classes = classes[24:32]
    fri_classes = classes[32:40]
    sat_classes = classes[40:48]

    context = {
        'mon_classes': mon_classes,
        'tue_classes': tue_classes,
        'wed_classes': wed_classes,
        'thu_classes': thu_classes,
        'fri_classes': fri_classes,
        'sat_classes': sat_classes,
    }

    return render(request, 'classes/times.html', context)


@login_required
def add_class(request):
    """ A view to add a new class """
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Successfully added class!')
            return redirect(reverse('all_classes'))
        else:
            messages.error(request, '''Failed to add class.
                           Please ensure the form is valid.''')
    else:
        form = ClassForm()

    template = 'classes/add_class.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_class(request, class_id):
    """ A view to edit existing classes """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only website owners can do that')
        return redirect(reverse('home'))

    singleclass = get_object_or_404(Class, pk=class_id)

    if request.method == "POST":
        form = ClassForm(request.POST, instance=singleclass)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the class!')
            return redirect(reverse('all_classes'))
        else:
            messages.error(request, '''Failed to update the class.
                           Please ensure the form is valid.''')
    else:
        form = ClassForm(instance=singleclass)
        messages.info(request, 'You are editing class times')

    template = 'classes/edit_class.html'
    context = {
        'form': form,
        'singleclass': singleclass,
    }

    return render(request, template, context)


@login_required
def delete_class(request, class_id):
    """ A view to delete existing class """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only website owners can do that')
        return redirect(reverse('home'))

    singleclass = get_object_or_404(Class, pk=class_id)
    singleclass.delete()
    messages.success(request, 'Class deleted!')
    return redirect(reverse('all_classes'))
