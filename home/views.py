from django.shortcuts import render ,redirect
from .forms import PhoneNumberForm
from .models import User
from random import randint ,random
from .utils import send_code , verificationCodeForm



# Create your views here.
# def home(request):
#
#     return render(request , 'home/home.html')
#
# def register(request):
#     if request.method == 'POST':
#         form = PhoneNumberForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = PhoneNumberForm()
#
#     else:
#         form = PhoneNumberForm()
#
#     return render(request , 'home/register.html' , context={'form': form})

# def phone_number_view(request):
#     if request.method == 'POST':
#         form = PhoneNumberForm(request.POST)
#         if form.is_valid():
#             phone_number = form.cleaned_data['phone_number']
#             name = form.cleaned_data['name']
#             user, created = User.objects.get_or_create(phone_number=phone_number)
#             #token = str(randint(1000, 9999)) # کد تصادفی باید اینجا قرار بگیره
#             #user.verification_code = verification_code
#             user.save()
#
#             token = str(random.randint(1000, 9999))  # ایجاد کد تصادفی ۴ رقمی
#             send_verification_code(phone_number, token)  # مقدار 'token' ارسال شد
#
#             return redirect('code_view')
#     else:
#         form = PhoneNumberForm()
#
#     return render(request, 'home/register.html', {'form': form})
#
#
# def verify_code_view(request):
#     if request.method == 'POST':
#         form = verificationCodeForm(request.POST)
#         if form.is_valid():
#             verification_code = form.cleaned_data['verification_code']
#             try:
#                 user = User.objects.get(verification_code=verification_code)
#                 user.is_verified = True
#                 user.verification_code = ''
#                 user.save()
#                 return redirect('home')
#             except User.DoesNotExist:
#                 form.add_error('verification_code', 'Invalid code')
#     else:
#         form = verificationCodeForm()
#     return render(request, 'verify.html', {'form': form})
# import random
# from django.shortcuts import render, redirect
# from .forms import PhoneNumberForm, VerificationCodeForm
# from .models import User
# from .utils import send_verification_code  # مطمئن شوید که این تابع را وارد کرده‌اید

from django.shortcuts import render, redirect
from .forms import PhoneNumberForm, VerificationCodeForm
from .models import User
from random import randint
from .utils import send_code  # ایمپورت تابع ارسال پیامک

def phone_number_view(request):
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            name = form.cleaned_data.get('name', '')  # دریافت نام در صورت وجود

            # دریافت یا ایجاد کاربر با شماره تلفن
            user, created = User.objects.get_or_create(phone_number=phone_number)
            if created:
                user.name = name  # اگر کاربر جدید است، نام را ذخیره می‌کنیم
                user.save()

            # ایجاد کد تأیید تصادفی
            token = str(randint(1000, 9999))  # ایجاد یک کد ۴ رقمی
            user.verification_code = token  # ذخیره کد تأیید در مدل کاربر
            user.save()

            # ارسال پیامک تأیید
            send_code(phone_number, token)  # ارسال شماره و کد تأیید به تابع

            # ذخیره شماره در سشن برای مرحله بعد
            request.session['phone_number'] = phone_number
            return redirect('code_view')  # هدایت به صفحه تایید کد
    else:
        form = PhoneNumberForm()

    return render(request, 'home/register.html', {'form': form})


