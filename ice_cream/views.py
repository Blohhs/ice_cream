from django.shortcuts import get_object_or_404, render

from .models import IceCream


def ice_cream_list(request):
    template_name = 'ice_cream/list.html'
    ice_cream_catalog = IceCream.objects.filter(is_published=True)
    context = {
        'ice_cream_catalog': ice_cream_catalog,
    }
    return render(request, template_name, context)


def ice_cream_detail(request, pk):
    template_name = 'ice_cream/detail.html'
    ice_cream = get_object_or_404(
        IceCream.objects.values(
            'title', 'description'
        ).filter(is_published=True),
        pk=pk
    )
    context = {
        'ice_cream': ice_cream,
    }
    return render(request, template_name, context)