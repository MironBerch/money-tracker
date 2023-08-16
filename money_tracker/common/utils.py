from unidecode import unidecode

from django.utils.text import slugify


def create_slug(slug: str) -> str:
    """Return slug with english pronounce."""
    return slugify(unidecode(slug))
