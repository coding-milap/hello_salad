from django.shortcuts import render,HttpResponseRedirect,reverse
from .forms import UserRegister,UserLogin,PasswordReset,UserForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login,logout,authenticate
from .models import User

def user_register(request):

    if request.method == "POST":

        form = UserRegister(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            form.save()

            form.save()
            send_mail(
            'Welcome Mail',
            f'Welcome, {first_name} {last_name}. Welcome to our Website TastySalad',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    
    form = UserRegister()

    return render(request,'register.html',{'form':form})

def user_login(request):

    if not request.user.is_authenticated:

        if request.method == "POST":

            form = UserLogin(request,data=request.POST)


            if form.is_valid():

                email = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username=email,password=password)
                

                if user:

                    login(request,user)

                    return HttpResponseRedirect(reverse('index'))


        form = UserLogin()

        return render(request,'user-login.html',{'form':form})
    else:

        return HttpResponseRedirect(reverse('index'))

def user_logout(request):

    logout(request)

    return HttpResponseRedirect(reverse('user-login'))

def forgot_password(request):

    if request.method == "POST":

        email = request.POST.get('email')
        user = User.objects.filter(email=email)[0]

        

        send_mail(
            'Reset Password',
            f'Please do not share this link with anyone!! https://healthylife.onrender.com/accounts/reset-password/{user.user_id}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )



    return HttpResponseRedirect(reverse("user-login"))

def reset_password(request,id):

    if request.method == "POST":

        form = PasswordReset(request.POST)

        if form.is_valid():

            password = form.cleaned_data['password']

            user = User.objects.get(pk=id)

            user.set_password(password)
            user.save()

            return HttpResponseRedirect(reverse('user-login'))

    form = PasswordReset()

    return render(request,'reset-password.html',{'form':form})


def contact(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            f'Query from {name}',
            f'{message}',
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )


    return render(request,'contact.html')

def user_profile(request):
    user = User.objects.filter(email=request.user)[0]

    if request.method == "POST":

        form = UserForm(request.POST,instance=user)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect(reverse('user-profile'))

    form = UserForm(instance=user)

    return render(request,'user-profile.html',{'form':form,'user':user})
