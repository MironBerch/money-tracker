from handlers.response import send_response
from services import get_user_categories
from telegram import Update
from telegram.ext import ContextTypes

from templates import render_template


async def categories_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = get_user_categories(
        url='/api/categories-list/',
        user_id=update.message.from_user.id,
    )
    await send_response(
        update,
        context,
        response=render_template(
            'categories_list.j2',
            {
                'categories': response,
            },
        ),
    )
