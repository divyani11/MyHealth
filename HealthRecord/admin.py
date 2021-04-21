from django.contrib import admin
from django.contrib.admin.decorators import register
from HealthRecord.models import H_User, Address, UserDetails

# Register your models here.

@register(H_User) 
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','username')

    def __str__(self):
        return super().__str__()

#admin.site.register(H_User, UserAdmin) # you can register models like this as well

@register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street','city', 'postal_code','province','country')

    def __str__(self):
        return super().__str__()


@register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('fname','lname', 'email','dateOfBirth','phone','username')

    def __str__(self):
        return super().__str__()