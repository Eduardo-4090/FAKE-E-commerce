from django.contrib import admin
from .models import Category, Produtos, Galeria ,Cart, CartItem

class GaleriaImagem(admin.TabularInline):
    model =Galeria
    max_num = 5
    extra = 5

@admin.register(Produtos)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'category', 'valor',)
    list_filter = ('category',)
    search_fields = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}

    inlines=[GaleriaImagem]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Cart)
admin.site.register(CartItem)

