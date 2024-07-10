from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.api.views.auth import AskOTPView, RegisterView

router = DefaultRouter()

urlpatterns = [
    path(
        'ask-otp/',
        AskOTPView.as_view(),
        name='ask_otp'
    ),
    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),
]
