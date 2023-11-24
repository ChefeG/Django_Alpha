from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Districts, Category, DistrictsImage, Apartment, DistrictsNews, Reviews


class DistrictsImageInLine(admin.TabularInline):
    model = DistrictsImage
    extra = 1


class ApartmentInLine(admin.TabularInline):
    model = Apartment
    extra = 1


class DistrictsNewsInLine(admin.TabularInline):
    model = DistrictsNews
    extra = 1


class DistrictsAdminForm(forms.ModelForm):
    description = forms.CharField(
        label='Описание',
        widget=CKEditorUploadingWidget())

    class Meta:
        model = Districts
        fields = '__all__'


class DistrictsNewsAdminForm(forms.ModelForm):
    text = forms.CharField(
        label='Новости',
        widget=CKEditorUploadingWidget())

    class Meta:
        model = DistrictsNews
        fields = '__all__'


@admin.register(Districts)
class DistrictsAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'metro', 'price', 'draft')
    list_display_links = ['name']
    list_filter = ('name', 'price')
    list_editable = ('draft',)
    save_on_top = True
    form = DistrictsAdminForm
    inlines = [DistrictsImageInLine, ApartmentInLine, DistrictsNewsInLine]
    actions = ['publish', 'unpublish']

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change',)
    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width = "150">')

    get_image.short_description = 'Изображение'


@admin.register(DistrictsImage)
class DistrictsImageAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'slug')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width = "150">')

    get_image.short_description = 'Изображение'


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('apart_name', 'get_image', 'apart_price')

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.apart_image.url}" width = "150">')

    get_image.short_description = 'Изображение'


@admin.register(DistrictsNews)
class DistrictsNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'anons', 'image', 'date')
    form = DistrictsNewsAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.apart_image.url}" width = "150">')

    get_image.short_description = 'Изображение'


admin.site.register(Category)
admin.site.register(Reviews)

admin.site.site_title = 'Царь-Бог Борис'
admin.site.site_header = 'Его невьебенное высочество Борис Великолепный'
