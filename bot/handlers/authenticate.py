from handlers.response import send_response
from telegram import Update
from telegram.ext import ContextTypes

from config import PROJECT_FULL_DOMAIN
from templates import render_template


async def start_authenticate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    await send_response(
        update,
        context,
        response=render_template(
            'start_authenticate.j2',
            {
                'telegram_login_url': PROJECT_FULL_DOMAIN + ':8000' + '/settings/telegram-login/',
            },
        ),
    )
