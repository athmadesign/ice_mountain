# employees/admin.py
from django.contrib import admin
from .models import BillUpload

@admin.register(BillUpload)
class BillUploadAdmin(admin.ModelAdmin):
    list_display = ['product_number', 'staff_name', 'shop_name', 'employee', 'uploaded_at']
    list_filter = ['uploaded_at', 'shop_name']
    search_fields = ['product_number', 'bill_number', 'staff_name']