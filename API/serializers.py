from rest_framework import serializers
from HealthRecord.models import H_User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = H_User
        field = '__all__'
        fields = ['pk','first_name', 'last_name', 'email', 'username']
    
     