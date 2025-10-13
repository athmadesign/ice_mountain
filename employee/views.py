# employees/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EmployeeRegistrationForm, EmployeeLoginForm, BillUploadForm
from .models import BillUpload
from django.core.mail import send_mail
from django.conf import settings

def register_view(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = EmployeeRegistrationForm()
    
    return render(request, 'core/employee/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
    else:
        form = EmployeeLoginForm()
    
    return render(request, 'core/employee/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')

@login_required
def dashboard_view(request):
    # Get user's uploaded bills
    user_bills = BillUpload.objects.filter(employee=request.user).order_by('-uploaded_at')
    
    if request.method == 'POST':
        form = BillUploadForm(request.POST, request.FILES)
        if form.is_valid():
            bill_upload = form.save(commit=False)
            bill_upload.employee = request.user
            bill_upload.save()
            
            # Send email to owner
            send_bill_email(bill_upload)
            
            messages.success(request, 'Bill uploaded successfully and email sent to owner!')
            return redirect('dashboard')
    else:
        form = BillUploadForm()
    
    context = {
        'form': form,
        'user_bills': user_bills,
    }
    return render(request, 'core/employee/dashboard.html', context)

def send_bill_email(bill_upload):
    subject = f'New Bill Upload - {bill_upload.product_number}'
    message = f"""
    New bill has been uploaded by {bill_upload.employee.get_full_name() or bill_upload.employee.username}.
    
    Details:
    - Staff Name: {bill_upload.staff_name}
    - Shop Name: {bill_upload.shop_name}
    - Product Number: {bill_upload.product_number}
    - GPay Number: {bill_upload.gpay_number}
    - Bill Number: {bill_upload.bill_number}
    - Uploaded At: {bill_upload.uploaded_at}
    
    Please check the attached file in the admin panel.
    """
    
    # Send email to owner (configure EMAIL_HOST_USER in settings)
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.OWNER_EMAIL],  # Add owner's email in settings
        fail_silently=False,
    )

# def home_view(request):
#     return render(request, 'employees/home.html')