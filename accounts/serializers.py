from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email','Adresse','first_name',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        print(token)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
          
                instance.set_password(password)
                print(instance)
                instance.save()
        return instance

    class Meta:
        model = CustomUser
        fields = ('token', 'email','Adresse','first_name', 'password')