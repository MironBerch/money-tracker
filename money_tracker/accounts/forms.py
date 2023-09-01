from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    UserChangeForm,
    UserCreationForm,
)
from django.core.exceptions import ValidationError
from django.utils import timezone

from accounts.models import Profile, User
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

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingEmail',
                'placeholder': 'name@example.com',
            },
        ),
    )

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
        send_password_reset_link.delay(
            subject_template_name=subject_template_name,
            email_template_name=email_template_name,
            context=context,
            from_email=from_email,
            to_email=to_email,
            html_email_template_name=html_email_template_name,
        )


class SetPasswordForm(SetPasswordForm):
    """Custom set password form."""

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingPassword',
                'placeholder': 'Password',
            },
        ),
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingPassword',
                'placeholder': 'Confirm password',
            },
        ),
    )


class PasswordChangeForm(PasswordChangeForm):
    """Password change form."""

    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingPassword',
                'placeholder': 'Password',
            },
        ),
    )

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingPassword',
                'placeholder': 'Password',
            },
        ),
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingPassword',
                'placeholder': 'Confirm password',
            },
        ),
    )


class UserInfoForm(forms.ModelForm):
    """Form for editing user info."""

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

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )


class ProfileForm(forms.ModelForm):
    """Form for editing user profile."""

    class Meta:
        model = Profile
        fields = (
            'gender',
            'date_of_birth',
        )
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',
                },
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-select',
                    'aria-label': 'Select category for transaction',
                    'id': 'floatingInput',
                },
            ),
        }

    def clean_date_of_birth(self):
        """Handles input of date_of_birth field.

        date of birth can't be in the future, Host must be at least 14 years old
        """
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth:
            date_now = timezone.now().date()
            year_diff = (date_now.month, date_now.day) < (date_of_birth.month, date_of_birth.day)
            host_age = date_now.year - date_of_birth.year - year_diff
            if date_of_birth > date_now:
                raise ValidationError(
                    'Invalid date: date of birth in the future.',
                    code='invalid',
                )
            elif host_age < 14:
                raise ValidationError(
                    'Invalid date: You must be at least 14 years old.',
                    code='underage',
                )
        return date_of_birth


class ProfileImageForm(forms.ModelForm):
    """Form for uploading profile image."""

    class Meta:
        model = Profile
        fields = ('profile_image', )
        widgets = {
            'profile_image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'type': 'file',
                    'id': 'formFile',
                },
            ),
        }


class ProfileDescriptionForm(forms.ModelForm):
    """Form for editing user description ('about me' section)."""

    class Meta:
        model = Profile
        fields = ('description', )
