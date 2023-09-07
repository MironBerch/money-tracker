from os import environ
from pathlib import Path

TELEGRAM_API_TOKEN = environ.get('TELEGRAM_API_TOKEN')

BASE_DIR = Path(__file__).resolve().parent

TEMPLATES_DIR = BASE_DIR / 'templates'

DATE_FORMAT = '%d.%m.%Y'

PROJECT_FULL_DOMAIN = environ.get('PROJECT_FULL_DOMAIN')
