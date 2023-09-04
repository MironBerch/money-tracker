from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.models import User


class SignupSerializer(serializers.ModelSerializer):
    """Signup API view serializer."""

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    first_name = serializers.CharField(
        required=True,
        max_length=30,
    )
    last_name = serializers.CharField(
        required=True,
        max_length=30,
    )
    password = serializers.CharField(
        min_length=8,
        write_only=True,
    )

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'password',
        )


class SigninSerializer(serializers.Serializer):
    """Signin API view serializer."""

    email = serializers.CharField(
        required=True,
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
    )
