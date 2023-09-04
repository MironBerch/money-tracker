from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login, logout

from accounts.api.serializers import SigninSerializer, SignupSerializer
from accounts.permissions import IsNotAuthenticated


class SignupAPIView(APIView):
    """Signup API view."""

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
