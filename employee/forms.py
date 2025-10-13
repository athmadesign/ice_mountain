# employees/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import BillUpload

class EmployeeRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(EmployeeRegistrationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})

class EmployeeLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeLoginForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})


class BillUploadForm(forms.ModelForm):
    class Meta:
        model = BillUpload
        fields = ['staff_name', 'shop_name', 'product_number', 'gpay_number', 'bill_number', 'bill_file']
        widgets = {
            'staff_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter staff name'}),
            'shop_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter shop name'}),
            'product_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product number'}),
            'gpay_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter GPay number'}),
            'bill_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter bill number'}),
            'bill_file': forms.FileInput(attrs={'class': 'form-control'}),
        }