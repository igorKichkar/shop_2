from django.shortcuts import render
from django.views.generic import DetailView

from .models import *


def main(request):
    return render(request, 'mainapp/base.html')


class ProductDetailViewes(DetailView):
    CT_MODEL_CLASS = {
        'smartfony': Smartphone,
        'noutbuki': Notebook,
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model.objects.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'mainapp/product_detail.html'
    slug_url_kwarg = 'slug'
