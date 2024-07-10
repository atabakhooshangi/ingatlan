from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
from user.models.base import Base


class OTP(Base):
    email = models.EmailField(
        verbose_name='Email',
        max_length=65,
        blank=False,
        null=False)
    otp_code = models.CharField(
        verbose_name='OTP code',
        max_length=128,
    )
    expired = models.BooleanField(
        verbose_name='Expired',
        default=False,
    )

    def __str__(self):
        return f'{self.email} - {self.otp_code}'

    class Meta:
        verbose_name = 'OTP'
        verbose_name_plural = 'OTPs'
        ordering = ('-created_at',)

    def is_valid(self):
        if self.expired:
            return False
        if timezone.now() > self.created_at + datetime.timedelta(minutes=int(settings.OTP_EXPIRE_MINUTES)):
            self.expired = True
            self.save()
            return False
        return True
