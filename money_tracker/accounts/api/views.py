from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.backends.db import SessionStore

from accounts.api.serializers import SigninSerializer, SignupSerializer, TelegramCodeSerializer
from accounts.permissions import IsNotAuthenticated
from accounts.services import get_user_by_telegram_code, set_user_telegram_id


class SignupAPIView(APIView):
    """Signup API view."""

    permission_classes = (IsNotAuthenticated,)
    serializer_class = SignupSerializer

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            login(request, user)
            return Response(
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class SigninAPIView(APIView):
    """Signin API view."""

    permission_classes = (IsNotAuthenticated,)
    serializer_class = SigninSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(
            request=request,
            email=email,
            password=password,
        )

        if user is not None:
            login(request, user)
            return Response(
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data={
                    'message': 'Invalid email or password',
                },
            )


class SignoutAPIView(APIView):
    """Signout API view."""

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TelegramCodeAPIView(APIView):
    """API view for set telegram id to user settings."""

    serializer_class = TelegramCodeSerializer

    def post(self, request):
        telegram_code = request.data.get('telegram_code')
        telegram_id = request.data.get('telegram_id')

        user = get_user_by_telegram_code(telegram_code=telegram_code)

        if user and set_user_telegram_id(user=user, telegram_id=telegram_id):
            login(request, user)
            session = SessionStore(session_key=request.session.session_key)

            return Response(
                status=status.HTTP_200_OK,
                data={
                    'session_key': session.session_key,
                },
            )

        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data={
                'message': 'Invalid telegram code',
            },
        )
