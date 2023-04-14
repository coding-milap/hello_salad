from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('about-us',views.about,name="about-us"),
    path('membership-plans',views.membership,name="membership-plans"),
    path('checkout-session/<str:id>',views.checkout,name="checkout-session"),
    path("success/<str:id>",views.success,name="success"),
    path('cancel',views.cancel,name="cancel")
]