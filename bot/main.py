import logging

from telegram.ext import ApplicationBuilder

from config import TELEGRAM_API_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO,
)
logger = logging.getLogger(__name__)


if not TELEGRAM_API_TOKEN:
    raise ValueError(
        "TELEGRAM_API_TOKEN env variables wasn't implemented in .env (both should be initialized).",
    )


def main():
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    application.run_polling()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
