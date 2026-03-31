from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, Additional, ProductImage, Comment


admin.site.site_header = "BurgerHouse"
admin.site.site_title = "BurgerHouse"
admin.site.index_title = "AdminSahifasi"
admin.site.login_template = "admin/login.html"


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    # readonly_fields = ('image',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'preparation_time', 'category', 'get_image')
    list_editable = ('category',)
    list_filter = ('category',)
    list_display_links = ('name',)
    search_fields = ('name', 'description', 'category__name')
    inlines = [
        ProductImageInline
    ]
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description="Rasmi")
    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.get_image()}" width="150">')

    # get_image.short_description = 'Rasmi'


admin.site.register([Category, Additional, Comment])
