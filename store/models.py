from django.db import models
from cloudinary.models import CloudinaryField
from accounts.models import User
import uuid
import datetime
from datetime import datetime as dt
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

today = datetime.date.today()

class Salad(models.Model):

    salad_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    salad_name = models.CharField(max_length=100)
    salad_price = models.PositiveIntegerField()
    salad_desc = models.TextField()
    salad_image = CloudinaryField('salad')


    def __str__(self):

        return self.salad_name

class Membership(models.Model):

    CHOICES = (('Weekly','Weekly'),
               ('Monthly','Monthly'))

    membership_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    membership_type = models.CharField(choices=CHOICES,max_length=200)
    duration = models.PositiveIntegerField(default=7)
    price = models.PositiveIntegerField()

    def __str__(self):

        return self.membership_type

class UserMembership(models.Model):

    uid = models.UUIDField(default=uuid.uuid4,primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="usermembership")
    membership = models.OneToOneField(Membership,on_delete=models.CASCADE,related_name="usermembership")


    def __str__(self):

        return self.user.email


class Subscription(models.Model):

    subscription_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    user_membership = models.OneToOneField(UserMembership,on_delete=models.CASCADE,related_name="subscription")
    expires_in = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):

        return self.user_membership.user.email

@receiver(post_save,sender=UserMembership)
def create_subscription(sender,instance,*args,**kwargs):

    if instance:

         Subscription.objects.create(user_membership=instance,expires_in=dt.now().date()+ timedelta(days=instance.membership.duration))

@receiver(post_save,sender=Subscription)
def subscription_update(sender,instance,*args,**kwargs):

    if today > instance.expires_in:

        subscription = Subscription.objects.get(pk=instance.subscription_id)
        subscription.delete()