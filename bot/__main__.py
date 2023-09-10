import logging

from handlers import authenticate_handler, categories_list, start, transactions_list
from telegram.ext import ApplicationBuilder, CommandHandler

from config import TELEGRAM_API_TOKEN

COMMAND_HANDLERS = {
    'start': start,
    'transactions_list': transactions_list,
    'categories_list': categories_list,
}

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO,
)
logger = logging.getLogger(__name__)


if not TELEGRAM_API_TOKEN:
    raise ValueError(
        'TELEGRAM_API_TOKEN env variables was not implemented in .env.',
    )


def main():
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    for command_name, command_handler in COMMAND_HANDLERS.items():
        application.add_handler(CommandHandler(command_name, command_handler))
    application.add_handler(authenticate_handler)

    application.run_polling()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
