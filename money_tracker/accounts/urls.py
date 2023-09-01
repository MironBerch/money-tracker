from django.urls import path

from accounts.views import (
    AccountSettingsDashboardView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
    PersonalInfoEditView,
    ProfileView,
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

    # password change urls
    path(
        route='password_change/',
        view=PasswordChangeView.as_view(),
        name='password_change',
    ),
    path(
        route='password_change/done/',
        view=PasswordChangeDoneView.as_view(),
        name='password_change_done',
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

    # profile urls
    path(
        route='profile/<int:pk>/',
        view=ProfileView.as_view(),
        name='profile_view',
    ),

    # settings urls
    path(
        route='settings/',
        view=AccountSettingsDashboardView.as_view(),
        name='settings_dashboard',
    ),
    path(
        route='settings/personal-info/',
        view=PersonalInfoEditView.as_view(),
        name='user_info_edit',
    ),
]
