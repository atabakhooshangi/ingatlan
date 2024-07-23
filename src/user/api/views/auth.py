from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from drf_yasg.utils import swagger_auto_schema

from user.models import User
from user.serializers.otp import AskOTPSerializer
from user.serializers.user import RegisterSerializer, LoginSerializer


class AuthenticationViewSet(GenericViewSet, ListModelMixin):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    # serializer_class = RegisterSerializer

    def get_serializer_class(self):
        if self.action == 'register':
            return RegisterSerializer
        if self.action == 'otp':
            return AskOTPSerializer
        if self.action == 'login':
            return LoginSerializer
        return super().get_serializer_class()

    @swagger_auto_schema(request_body=RegisterSerializer)
    @action(detail=False, methods=["POST"])
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=AskOTPSerializer)
    @action(detail=False, methods=["POST"])
    def otp(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=LoginSerializer)
    @action(detail=False, methods=["POST"])
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.get_tokens()
        return Response(tokens, status=status.HTTP_201_CREATED)
