from random import randint
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, SignInForm
from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from .models import EmailVerified



def register(request):
    template_name = "custom_sign/signup.html"
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            EmailAddress(email=email, user=User.objects.get(email=email), primary=True).save()
            while True:
                try:
                    password = randint(100000, 999999)
                    EmailVerified(email=EmailAddress.objects.get(email=email), password=password).save()
                    break
                except:
                    continue
            verified = EmailVerified.objects.get(password=password)
            EmailVerified.email_verified(verified)
            return redirect('verified')
    form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


def verified(request):
    template_name = "custom_sign/verified.html"
    context = {}
    if request.method == 'POST':
        print(request.POST.get('password'))
        try:
            emailverified = EmailVerified.objects.get(password=request.POST.get('password'))
            emailverified.email.verified = True
            emailverified.email.save()
            emailverified.delete()
            return redirect('user')
        except:
            return redirect('verified')

    return render(request, template_name, context)


def signin(request):
    template_name = "custom_sign/sign_in.html"
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email.lower()).username
        user = authenticate(username=username, password=password)
        if user:
            if EmailAddress.objects.get(email=email).verified:
                login(request, user)
                return redirect('user')
        return redirect('verified')
    context = {
        'form': SignInForm,
    }
    return render(request, template_name, context)
