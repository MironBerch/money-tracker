from typing import Optional

from celery import shared_task

from accounts.services import get_user_by_pk, send_password_reset_email


@shared_task
def send_password_reset_link(
        subject_template_name: str,
        email_template_name: str,
        context: dict,
        from_email: str,
        to_email: str,
        html_email_template_name: Optional[str] = None,
) -> None:
    """Send password reset email celery task."""
    context['user'] = get_user_by_pk(pk=context['user'])
    send_password_reset_email(
        subject_template_name=subject_template_name,
        email_template_name=email_template_name,
        context=context,
        from_email=from_email,
        to_email=to_email,
        html_email_template_name=html_email_template_name,
    )


@shared_task
def delete_telegram_verify_code(id):
    """Delete user telegram verify code after 10 minutes from creating."""
    from .models import TelegramUserVerifyCode

    try:
        TelegramUserVerifyCode.objects.get(id=id).delete()
    except TelegramUserVerifyCode.DoesNotExist:
        pass
