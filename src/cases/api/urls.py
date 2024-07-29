from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cases.api.views.case import CaseViewSet

router = DefaultRouter()

router.register(
    prefix="case",
    viewset=CaseViewSet,
    basename="auth"
)

urlpatterns = [
    path('', include(router.urls)),
]
