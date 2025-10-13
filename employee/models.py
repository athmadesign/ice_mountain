# employees/models.py
from django.contrib.auth.models import User
from django.db import models

class BillUpload(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=200)
    product_number = models.CharField(max_length=100)
    gpay_number = models.CharField(max_length=15)
    bill_number = models.CharField(max_length=100)
    bill_file = models.FileField(upload_to='bills/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_number} - {self.staff_name}"