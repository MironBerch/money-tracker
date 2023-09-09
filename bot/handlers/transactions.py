from handlers.response import send_response
from services import get_user_session_key, session
from telegram import Update
from telegram.ext import ContextTypes

from templates import render_template


async def transactions_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session_key = get_user_session_key(user_id=update.message.from_user.id)
    session.cookies.set('sessionid', session_key)
    response = session.get(
        url='http://server:8000' + '/api/transactions-list/',
    )
    response = response.json()
    await send_response(
        update,
        context,
        response=render_template(
            'transactions_list.j2',
            {
                'transactions': response,
            },
        ),
    )
