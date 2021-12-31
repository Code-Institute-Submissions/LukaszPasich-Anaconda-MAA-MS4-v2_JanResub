from django.shortcuts import render
from .models import Class
from django.contrib.auth.decorators import login_required

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


@login_required
def edit_classes(request):
    """ Edit classes """

    form = Class.objects.all()

    template = 'classes/edit_classes.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry, only website owners can do that')
    #     return redirect(reverse('home'))

    # product = get_object_or_404(Product, pk=product_id)
    # if request.method == 'POST':
    #     form = ProductForm(request.POST, request.FILES, instance=product)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Product updated successfully!')
    #         return redirect(reverse('product_detail', args=[product.id]))
    #     else:
    #         messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    # else:
    #     form = ProductForm(instance=product)
    #     messages.info(request, f'You are editing {product.name}')

    # template = 'products/edit_product.html'
    # context = {
    #     'form': form,
    #     'product': product,
    # }

    # return render(request, template, context)