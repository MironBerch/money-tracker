from random import randint

from django.shortcuts import get_object_or_404
from django.template.loader import get_template, render_to_string

from accounts.models import Settings, TelegramUserVerifyCode, User
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


def check_that_code_with_this_value_does_not_exist(code: int) -> bool:
    """Check that code with this value does not exist."""
    return not TelegramUserVerifyCode.objects.filter(telegram_code=code).exists()


def create_unique_telegram_authentication_code(user: User) -> TelegramUserVerifyCode:
    """Create unique telegram authentication code."""
    while True:
        telegram_code = randint(100000, 999999)
        if check_that_code_with_this_value_does_not_exist(code=telegram_code):
            return TelegramUserVerifyCode.objects.create(
                telegram_code=telegram_code,
                user=user,
            )


def get_telegram_authentication_code(user: User) -> TelegramUserVerifyCode:
    """Get old or create a new telegram authentication code."""
    try:
        code = TelegramUserVerifyCode.objects.get(user=user)
    except TelegramUserVerifyCode.DoesNotExist:
        code = create_unique_telegram_authentication_code(user=user)
    return code


def get_user_by_telegram_code(telegram_code: str) -> User | None:
    """Get user by telegram code or return `None`."""
    try:
        return (
            TelegramUserVerifyCode.objects.get(
                telegram_code=telegram_code,
            ).user
        )
    except TelegramUserVerifyCode.DoesNotExist:
        return None


def set_user_telegram_id(user: User, telegram_id: str) -> bool:
    """Set telegram id to user settings."""
    try:
        settings = Settings.objects.get(user=user)
        settings.telegram_id = telegram_id
        settings.save()
        return True
    except Settings.DoesNotExist:
        return False
