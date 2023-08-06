from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from accounts.models import User


class SignUpForm(UserCreationForm):
    """Form for signing up/creating new account."""

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
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'


class AdminUserChangeForm(UserChangeForm):
    """Form for editing `User` (used on the admin panel)."""

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )
