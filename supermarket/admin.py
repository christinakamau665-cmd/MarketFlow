from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category, Supplier, Sale, CustomerChat


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_person', 'phone', 'email']
    search_fields = ['name', 'contact_person']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'barcode_number', 'barcode_preview', 'category', 'price', 'stock_quantity', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'sku', 'barcode_number']
    readonly_fields = ['barcode_preview']

    def barcode_preview(self, obj):
        if obj.barcode_image:
            return format_html('<img src="{}" style="height:40px;width:auto;" />', obj.barcode_image.url)
        return '-'
    barcode_preview.short_description = 'Barcode'


@admin.register(CustomerChat)
class CustomerChatAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_phone', 'customer_email', 'product', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['customer_name', 'customer_phone', 'customer_email', 'subject', 'message']
    readonly_fields = ['created_at', 'responded_at']


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity_sold', 'unit_price', 'total_amount', 'sale_date', 'cashier']
    list_filter = ['sale_date']
    search_fields = ['product__name', 'cashier']
