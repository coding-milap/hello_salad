from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from cloudinary.models import CloudinaryField
import uuid

class UserManager(BaseUserManager):


    def create_user(self,email,password,**extra_fields):

        if not email:

            return ValueError("Email must be there")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(self.db)

        return user
    
    def create_superuser(self,email,password,**extra_fields):

        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:

            raise ValueError(("Super user must have is_staff True. "))

        return self.create_user(email,password,**extra_fields)

class User(AbstractUser):

    username = None
    user_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    mobile = models.CharField(max_length=14,unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    avatar = CloudinaryField('avatar')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):

        return self.email