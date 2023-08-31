from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.views.generic.base import TemplateResponseMixin

from accounts.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    SignUpForm,
)
from accounts.mixins import AnonymousUserRequiredMixin
from accounts.services import get_user_by_pk


class SignUpView(
    AnonymousUserRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """View for creating a new account."""

    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response(
            context={
                'form': self.form_class(),
            },
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('signin')

        return self.render_to_response(
            context={
                'form': form,
            },
        )


class SignInView(
    AnonymousUserRequiredMixin,
    LoginView,
):
    """View for signing in."""

    form_class = AuthenticationForm
    template_name = 'registration/signin.html'


class SignOutView(LogoutView):
    """View for signing out."""

    template_name = 'registration/signout.html'
    next_page = None


class PasswordResetView(PasswordResetView):
    """View for resetting a password."""

    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('password_reset_done')
    html_email_template_name = 'registration/password_reset_email.html'
    email_template_name = 'registration/password_reset_email.html'
    form_class = PasswordResetForm


class PasswordResetDoneView(PasswordResetDoneView):
    """View for show that resetting a password is done."""

    template_name = 'registration/password_reset_done.html'


class PasswordResetConfirmView(PasswordResetConfirmView):
    """View for confirm resetting a password."""

    form_class = SetPasswordForm
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


class PasswordResetCompleteView(PasswordResetCompleteView):
    """View for show that resetting a password is complete."""

    template_name = 'registration/password_reset_complete.html'


class PasswordChangeView(PasswordChangeView):
    """View for changing a password."""

    form_class = PasswordChangeForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_change_done')


class PasswordChangeDoneView(PasswordChangeDoneView):
    """View for show that changing a password is complete."""

    template_name = 'registration/password_change_done.html'


class ProfileView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """User profile view."""

    template_name = 'profile/profile.html'

    def get(self, request: HttpRequest, pk: int, *args, **kwargs):
        return self.render_to_response(
            context={
                'profile_owner': get_user_by_pk(pk=pk),
            },
        )


class AccountSettingsDashboardView(
    LoginRequiredMixin,
    TemplateView,
):
    """View for showing an account dashboard."""

    template_name = 'settings/settings_dashboard.html'
