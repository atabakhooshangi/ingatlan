from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenVerifyView

from user.api.views.auth import AuthenticationViewSet

router = DefaultRouter()

router.register(
    prefix="auth",
    viewset=AuthenticationViewSet,
    basename="auth"
)

urlpatterns = [
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
]
