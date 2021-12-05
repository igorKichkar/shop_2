from django.contrib import admin
from django.forms import ModelForm, ValidationError

from .models import *


class ProductAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Загружайте изображение с минимальным изображением {} * {}'.format(
            *Product.MIN_RESOLUTION)

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_width, min_height = Product.MIN_RESOLUTION
        max_width, max_height = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения превышает 3МВ')
        if img.width < min_width or img.height < min_height:
            raise ValidationError('Разрешение изображения меньше минимального')
        if img.width > max_width or img.height > max_height:
            raise ValidationError('Разрешение изображения больше максимального')
        return image


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class NotebookAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    prepopulated_fields = {'slug': ('title',)}


class SmartphoneAdminForm(ProductAdminForm, ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and not instance.sd:
            self.fields['sd_volume_max'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgray;'
            })

    def clean(self):
        if not self.cleaned_data['sd']:
            self.cleaned_data['sd_volume_max'] = None
        return self.cleaned_data


class SmartphoneAdmin(admin.ModelAdmin):
    change_form_template = 'mainapp/admin.html'
    form = SmartphoneAdminForm

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Customer)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
