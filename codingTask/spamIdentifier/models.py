from django.db import models
# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, name, password=None, email=None):
        if not phone_number:
            raise ValueError('Users must have a phone number')
        
        user = self.model(
            phone_number=phone_number,
            name=name,
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, password, email=None):
        user = self.create_user(
            phone_number=phone_number,
            name=name,
            password=password,
            email=email,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class RegisteredUser(AbstractBaseUser):
    username=None
    phone_number = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=255, blank=False,null=False)
    password = models.CharField(max_length=10,blank=False)
    email = models.EmailField(max_length=20,blank=True,null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

   
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.phone_number

class Contact(models.Model):
    registered_user = models.ForeignKey(RegisteredUser,on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=255)
    contact_phone_number = models.CharField(max_length=15)

    class Meta:
        unique_together = ('registered_user','contact_phone_number')


class SpamReport(models.Model):
    phone_number = models.CharField(max_length=15)
   