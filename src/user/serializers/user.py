from rest_framework import serializers
import random

from user.models import OTP, User
from user.utils.utils import check_otp


class RegisterSerializer(serializers.ModelSerializer):
    otp_code = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'otp_code',
                  'last_name', 'gender', 'phone_number',
                  'province', 'city', 'birthday',
                  ]

        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'phone_number': {'required': False},
            'province': {'required': False},
            'city': {'required': False},
            'birthday': {'required': False},
        }

    def validate(self, attrs):
        user = User.objects.filter(email=attrs['email'])
        if user.exists():
            raise serializers.ValidationError({'email': ['User with this email already exists.']})
        otp = check_otp(attrs['email'], attrs['otp_code'])
        if otp:
            return attrs
        raise serializers.ValidationError({'OTP': ['Invalid OTP Code.']})

    def save(self, **kwargs):
        data = self.validated_data.copy()
        user = User.objects.create_user(
            email=data.get('email'),
            password=data.pop('password'),

        )
        for key, value in data.items():
            setattr(user, key, value)
        user.save()

        return user
