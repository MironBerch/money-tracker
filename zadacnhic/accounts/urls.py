from django.urls import path

from accounts.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
    SignInView,
    SignOutView,
    SignUpView,
)

urlpatterns = [
    path(
        route='signup/',
        view=SignUpView.as_view(),
        name='signup',
    ),
    path(
        route='signin/',
        view=SignInView.as_view(),
        name='signin',
    ),
    path(
        route='signout/',
        view=SignOutView.as_view(),
        name='signout',
    ),

    # password reset urls
    path(
        'password_reset/',
        PasswordResetView.as_view(),
        name='password_reset',
    ),
    path(
        route='password_reset/done/',
        view=PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        route='reset/<uidb64>/<token>/',
        view=PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        route='reset/done/',
        view=PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
]
