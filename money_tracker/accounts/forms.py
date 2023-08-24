from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    UserChangeForm,
    UserCreationForm,
)

from accounts.models import User
from accounts.tasks import send_password_reset_link


class SignUpForm(UserCreationForm):
    """Form for signing up/creating new account."""

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingEmail',
                'placeholder': 'name@example.com',
            },
        ),
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingName',
                'placeholder': 'Name',
            },
        ),
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingSurname',
                'placeholder': 'Surname',
            },
        ),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingPassword1',
                'placeholder': 'Password',
            },
        ),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingPassword2',
                'placeholder': 'Confirm password',
            },
        ),
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'
        self.fields['first_name'].label = 'Name'
        self.fields['last_name'].label = 'Surname'


class AuthenticationForm(AuthenticationForm):
    """Custom Authentication form."""

    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': 'name@example.com',
            },
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingPassword',
                'placeholder': 'Password',
            },
        ),
    )


class AdminUserChangeForm(UserChangeForm):
    """Form for editing `User` (used on the admin panel)."""

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )


class PasswordResetForm(PasswordResetForm):
    """
    Custom password reset form.

    Send emails using Celery.
    """

    def send_mail(
            self,
            subject_template_name,
            email_template_name,
            context,
            from_email,
            to_email,
            html_email_template_name=None,
    ):
        context['user'] = context['user'].pk
        send_password_reset_link(
            subject_template_name=subject_template_name,
            email_template_name=email_template_name,
            context=context,
            from_email=from_email,
            to_email=to_email,
            html_email_template_name=html_email_template_name,
        )
