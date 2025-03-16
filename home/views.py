from django.shortcuts import render, redirect
from .forms import PhoneNumberForm, VerificationCodeForm
from .models import User
from random import randint
from .utils import send_code


def home(request):
    return render(request, 'home/home.html')


def welcome(request):
    return render(request, 'home/welcome.html')


def phone_number_view(request):
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            name = form.cleaned_data.get('name', '')  # دریافت نام در صورت وجود

            # ایجاد کد تأیید تصادفی و ذخیره در سشن
            token = str(randint(1000, 9999))  # ایجاد یک کد ۴ رقمی
            request.session['phone_number'] = phone_number
            request.session['verification_code'] = token
            request.session['name'] = name

            send_code(phone_number, token)  # ارسال شماره و کد تأیید به تابع

            return redirect('code_view')  # هدایت به صفحه تایید کد

    else:
        form = PhoneNumberForm()

        return render(request, 'home/register.html', {'form': form})


def verify(request):
    if request.method == 'POST':
        form = VerificationCodeForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['verification_code']
            stored_code = request.session.get('verification_code')
            phone_number = request.session.get('phone_number')
            name = request.session.get('name')

            if entered_code == stored_code:
                # ذخیره اطلاعات کاربر بعد از تایید موفقیت‌آمیز کد
                user, created = User.objects.get_or_create(phone_number=phone_number)
                user.name = name  # در صورت نیاز، نام را ذخیره می‌کنیم
                user.save()

                # پاک کردن اطلاعات سشن
                request.session.pop('verification_code', None)
                request.session.pop('phone_number', None)
                request.session.pop('name', None)

                return redirect('welcome')
            else:
                form.add_error('verification_code', 'کد وارد شده اشتباه است')
    else:
        form = VerificationCodeForm()

    return render(request, 'home/verify.html', {'verify_form': form})

