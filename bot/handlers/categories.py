from handlers.response import send_response
from services import create_category, get_user_categories
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, ConversationHandler, MessageHandler

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


# State constants
START_CREATE, CREATE = range(2)


async def start_category_create(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    await send_response(
        update,
        context,
        response=render_template('start_category_create.j2'),
    )
    return CREATE


async def category_create(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    response = create_category(
        user_id=update.message.from_user.id,
        name=update.message.text,
    )
    await send_response(
        update,
        context,
        response=render_template(
            'category_create.j2',
            {
                'status_code': response.status_code,
            },
        ),
    )
    return ConversationHandler.END

category_create_handler = ConversationHandler(
    entry_points=[CommandHandler('category_create', start_category_create)],
    states={
        CREATE: [MessageHandler(None, category_create)],
    },
    fallbacks=[],
)
