from django.shortcuts import render,redirect
from . models import Salad,Membership,UserMembership
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings
from django.core.mail import send_mail

stripe.api_key = "sk_test_51MpWsISF1UWtETMmqDlFBb3jdcoCIxUTehYPpExJDkljreDwTqd3ZdRzFiFks9unBWvDS0YFEIk5OUQgM8bskxk100zIRrkJSG"


@login_required(login_url='/accounts/user-login')
def index(request):

    salads =  Salad.objects.all()

    return render(request,'index.html',{'salads':salads})

@login_required(login_url='/accounts/user-login')
def about(request):

    return render(request,'about.html')

@login_required(login_url='/accounts/user-login')
def membership(request):

    memberships = Membership.objects.all()

    return render(request,'membership.html',{'memberships':memberships})


@login_required(login_url='/accounts/user-login/')
def checkout(request,id):

    membership =  Membership.objects.get(pk=id)

    session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data':{
                    'currency':'inr',
                
                'product_data':{
                    'name': membership.membership_type,
                },
                'unit_amount': membership.price*100,
                },
                 'quantity': 1,
            }
        ],
        mode='payment',
        success_url=f'http://127.0.0.1:8000/success/{membership.membership_id}',
        cancel_url='http://127.0.0.1:8000/cancel',

    )

    return redirect(session.url, code=303)


@login_required(login_url='/accounts/user-login/')
def success(request,id):

    user = request.user
    membership = Membership.objects.get(pk=id)

    user_membership = UserMembership(user=user,membership=membership)
    user_membership.save()

    send_mail(
            'Order Confiremed',
            f'Hey, {user} your order is confirmed!!, Welcome to Our Salad Family. Hope you enjoy our salads...',
            settings.EMAIL_HOST_USER,
            [user],
            fail_silently=False,
        )



    return render(request,'success.html')


# When payment interrupted.
@login_required(login_url='/accounts/user-login/')
def cancel(request):

    return render(request,'cancel.html')