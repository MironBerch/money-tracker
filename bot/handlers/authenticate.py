import json

import requests
from handlers.response import send_response
from services import save_user_session_key
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, ConversationHandler, MessageHandler

from config import PROJECT_FULL_DOMAIN
from templates import render_template

# State constants
START_AUTH, AUTH = range(2)


async def start_authenticate(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    status_code = 0
    if response.status_code == 200:
        status_code = 200
        response = response.json()
        save_user_session_key(
            user_id=update.message.from_user.id,
            session_key=response.get('session_key'),
        )
    await send_response(
        update,
        context,
        response=render_template(
            'authenticate.j2',
            {
                'status_code': status_code,
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
