from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    # password = serializers.CharField(max_length=100, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'address', 'phone', 'image', 'password']
        write_only_fields = ('password',)
        read_only_fields = (['id'])
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):

        password = validated_data.pop('password')
        user = super(UserSerializers, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user
   
            

        

            

