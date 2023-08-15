from unidecode import unidecode


def slug_to_english(slug: str) -> str:
    """Return slug with english pronounce."""
    return unidecode(slug)
