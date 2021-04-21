from django.db import models
from django.db.models.deletion import SET_NULL
from phone_field import PhoneField

    
class Address(models.Model):
    street = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=120)
    province = models.CharField(max_length=120)
    country = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.province}, {self.country}"

class H_User(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    email = models.EmailField()
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=50,blank=False, default='')
    address =models.ForeignKey(Address, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

class UserDetails(models.Model):
    fname = models.CharField(max_length=150,help_text='First Name')
    lname = models.CharField(max_length=150,help_text='Last Name')
    email = models.EmailField(default='',blank=False, unique=True)
    dateOfBirth =  models.DateField(null=True, blank=True)
    phone = PhoneField(blank=True, help_text='Primary Phone Number')
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=50,blank=False,default='',help_text='Includes 8-12 chars, contains (0-9), (a-z), one capital letter')

    def __str__(self):
        return f"{self.username}"




