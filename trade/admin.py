from django.contrib import admin
from trade.models import Product,  TradeNode
from django.urls import reverse
admin.site.register(Product)
from django.utils.html import format_html
# admin.site.register(TradeNode)



@admin.register(TradeNode)
class TradeNodeAdmin(admin.ModelAdmin):
    # inlines = [AvailableProductsInline]
    list_display = ('name', 'supplier_link', 'city','debt_to_supplier', 'level')
    list_filter = ('city',)
    actions = ['clear_debt']
    # search_fields = ('name', 'email', 'country', 'city', 'street', 'house_number')
    def supplier_link(self, obj):
        if obj.supplier:
            return format_html('<a href="{}">{}</a>', admin_url(obj.supplier), obj.supplier.name)
        return 'None'

    supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0.00)

    clear_debt.short_description = "Очистить задолженность у выбранных объектов"

# Register your models here.

def admin_url(obj):
    return reverse(f"admin:{obj._meta.app_label}_{obj._meta.model_name}_change", args=[obj.id])