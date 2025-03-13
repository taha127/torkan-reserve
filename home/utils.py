from django import forms
import requests  # اطمینان حاصل کنید که این خط وارد شده باشد

def send_code(phone_number, token):
    api_key = "***REMOVED***"
    url = f"https://api.kavenegar.com/v1/{api_key}/verify/lookup.json"

    params = {
        "receptor": phone_number,
        "token": token,
        "template": "verify"
    }
    try:
        response = requests.get(url, params=params)
        # بررسی وضعیت کد پاسخ API
        if response.status_code == 200:
            return response.json()  # پاسخ API را برمی‌گرداند
        else:
            # در صورتی که پاسخ موفق نباشد، محتوای خطا را برای عیب‌یابی چاپ کنید
            return {"error": f"Failed to send verification code: {response.text}"}
    except Exception as e:
        # در صورت بروز خطا در اتصال به API، خطا را ثبت می‌کنیم
        return {"error": f"Exception occurred: {str(e)}"}


class VerificationCodeForm(forms.Form):
    verification_code = forms.CharField(max_length=4, required=True)  # الزامی بودن وارد کردن کد
