from rest_framework import serializers
import random

from user.models import OTP


class AskOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True, required=True)
    otp_code = serializers.IntegerField(read_only=True)

    @staticmethod
    def otp_generator():
        return random.randint(10000, 99999)

    def validate(self, attrs):
        attrs['otp_code'] = self.otp_generator()
        return super().validate(attrs)

    def save(self, **kwargs):
        check_last_otp: OTP = OTP.objects.filter(email=self.validated_data['email'], expired=False).last()
        if check_last_otp:
            if check_last_otp.is_valid():
                return check_last_otp
        new_otp = OTP(
            email=self.validated_data['email'],
            otp_code=self.validated_data['otp_code']
        )
        new_otp.save()
        # TODO: send email logic
        return new_otp
