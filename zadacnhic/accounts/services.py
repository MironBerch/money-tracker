from django.shortcuts import get_object_or_404
from django.template.loader import get_template, render_to_string

from accounts.models import User
from mailings.services import send_email_with_attachments


def get_user_by_pk(pk: int | str) -> User | None:
    """Get `User` by primary key."""
    return get_object_or_404(User, pk=pk)


def get_user_by_email(email: str) -> User | None:
    """Get `User` by email."""
    return get_object_or_404(User, email=email)


def send_password_reset_email(
        *,
        subject_template_name: str,
        email_template_name: str,
        context: dict,
        from_email: str,
        to_email: str,
        html_email_template_name: str = None,
) -> None:
    """Send custom password reset email."""
    subject = render_to_string(subject_template_name, context)
    subject = ''.join(subject.splitlines())

    body = render_to_string(email_template_name, context)

    html = get_template(html_email_template_name)
    html_content = html.render(context)

    send_email_with_attachments(
        subject=subject,
        body=body,
        email_to=[to_email],
        email_from=from_email,
        alternatives=[(html_content, 'text/html')],
    )
