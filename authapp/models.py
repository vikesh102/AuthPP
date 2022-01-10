from django.db import models
from django.core import validators
from phone_field import PhoneField
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Userinfo(models.Model):
	Name = models.CharField(max_length = 100)
	Phone_Number = PhoneField(max_length=12)
	Password = models.CharField(max_length=20)
	Email = models.CharField(max_length = 100)
	Create_Date = models.DateTimeField(max_length = 100)
	Last_Updated = models.DateTimeField()
	Is_Active = models.BooleanField()


def save(self, *args, **kwargs):
	self.og_password=make_password(self.og_password)
	super(og, self).save(*args,**kwargs)


class Status(models.Model):
    INACTIVE = 0
    ACTIVE = 1
    STATUS = (
        (INACTIVE, _('Inactive')),
        (ACTIVE, _('Active')),
    )

    Is_Active  = models.BooleanField(default=0, choices=STATUS)