import json

import requests
from handlers.response import send_response
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, ConversationHandler, MessageHandler

from config import PROJECT_FULL_DOMAIN
from templates import render_template

# State constants
START_AUTH, AUTH = range(2)


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
    return AUTH


async def authenticate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    response = requests.post(
        url='http://server:8000' + '/api/telegram-auth/',
        data=json.dumps(
            {
                'telegram_id': update.message.from_user.id,
                'telegram_code': update.message.text,
            },
        ),
        headers={
            'Content-Type': 'application/json',
        },
    )
    await send_response(
        update,
        context,
        response=render_template(
            'authenticate.j2',
            {
                'status_code': response.status_code,
            },
        ),
    )
    return ConversationHandler.END

authenticate_handler = ConversationHandler(
    entry_points=[CommandHandler('authenticate', start_authenticate)],
    states={
        AUTH: [MessageHandler(None, authenticate)],
    },
    fallbacks=[],
)
