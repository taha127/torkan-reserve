from django.shortcuts import render
from .models import User
# Create your views here.
def home(request):

    return render(request , 'home/home.html')

def register(request):
    if request.method == "POST":
        pass
    else:
        form = User()
    return render(request , 'home/register.html' , {'form': form})