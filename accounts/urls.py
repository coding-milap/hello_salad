from django.urls import path
from . import views

urlpatterns = [

    path('user-profile',views.user_profile,name="user-profile"),
    path('user-register',views.user_register,name="user-register"),
    path('user-login',views.user_login,name="user-login"),
    path('user-logout',views.user_logout,name="user-logout"),
    path('forgot-password',views.forgot_password,name="forgot-password"),
    path('reset-password/<str:id>',views.reset_password,name="reset-password"),
    path('contact-us',views.contact,name="contact")

]