from django.urls import path

from accounts.views import SignInView, SignOutView, SignUpView

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
]
