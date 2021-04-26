from django import forms
from django.forms import fields
from HealthRecord.models import UserDetails

class Create_Account(forms.ModelForm):
   

    class Meta:
        model = UserDetails
        fields = ['fname', 'lname','email','dateOfBirth','phone','username']

