from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from drf_yasg.utils import swagger_auto_schema

from cases.models import Case
from cases.serializers import CaseSerializer


class CaseViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    permission_classes = (AllowAny,)
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    # serializer_class = RegisterSerializer

    # def get_serializer_class(self):
    #     if self.action == 'register':
    #         return RegisterSerializer
    #     if self.action == 'otp':
    #         return AskOTPSerializer
    #     if self.action == 'login':
    #         return LoginSerializer
    #     return super().get_serializer_class()
