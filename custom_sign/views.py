from random import randint
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, SignInForm
from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from .models import EmailVerified
from forum.management.commands.runapscheduler import my_job


def register(request):
    template_name = "custom_sign/signup.html"
    form = CustomUserCreationForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        try:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                email = request.POST.get('email').lower()
                EmailAddress(email=email, user=User.objects.get(email=email), primary=True).save()
                password = randint(100000, 999999)
                EmailVerified(
                    email=EmailAddress.objects.get(user=User.objects.get(email=email)),
                    password=password
                ).save()
                verified = EmailVerified.objects.get(password=password)
                EmailVerified.email_verified(verified)
                return redirect(f'/account/verified/?mail={email}')
        except ValidationError as e:
            context.update(exept=e)
        context.update(error=form.errors)
    return render(request, template_name, context)


def verified(request):
    if request.GET:
        template_name = "custom_sign/verified.html"
        context = {}
        if request.method == 'POST':
            if request.POST.get('posttype') == 'mail':
                try:
                    email = EmailAddress.objects.get(email=request.GET['mail'])
                    email = EmailVerified.objects.get(email=email)
                    EmailVerified.email_verified(email)
                except:
                    context.update(error='Ошибка')
            try:
                email = EmailAddress.objects.get(email=request.GET['mail'])
                emailverified = EmailVerified.objects.get(password=request.POST.get('password'), email=email)
                emailverified.email.verified = True
                emailverified.email.save()
                emailverified.delete()
                return redirect('user')
            except:
                context.update(ver='Пароль введён неправильно')

        return render(request, template_name, context)
    return redirect('main')



def signin(request):
    template_name = "custom_sign/signin.html"
    context = {
        'form': SignInForm,
    }
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            username = User.objects.get(email=email.lower()).username
            user = authenticate(username=username, password=password)
            if EmailAddress.objects.get(email=email).verified:
                login(request, user)
                return redirect('user')
            return redirect(f'/account/verified/?mail={email}')
        except:
            context.update(error='Введён неправильный email или пароль')
    return render(request, template_name, context)
