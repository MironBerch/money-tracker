from handlers.response import send_response
from services import get_user_transactions
from telegram import Update
from telegram.ext import ContextTypes

from templates import render_template


async def transactions_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = get_user_transactions(
        url='/api/transactions-list/',
        user_id=update.message.from_user.id,
    )
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


async def incomes_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = get_user_transactions(
        url='/api/incomes-list/',
        user_id=update.message.from_user.id,
    )
    await send_response(
        update,
        context,
        response=render_template(
            'incomes_list.j2',
            {
                'incomes': response,
            },
        ),
    )


async def expenses_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = get_user_transactions(
        url='/api/expenses-list/',
        user_id=update.message.from_user.id,
    )
    await send_response(
        update,
        context,
        response=render_template(
            'expenses_list.j2',
            {
                'expenses': response,
            },
        ),
    )
