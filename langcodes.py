import json

with open("langcodes.json") as fp:
    iso_639_languages = json.load(fp)


def get_language_name(language_code):
    """
    Returns the language name for a given ISO 639-1 language code.

    Parameters:
        language_code (str): Two-letter ISO 639-1 language code.

    Returns:
        str: Language name if code exists, otherwise an error message.
    """
    err_or_langcode = iso_639_languages.get(
        language_code, f"Language code '{language_code}' not found."
    )
    if isinstance(err_or_langcode, dict):
        return err_or_langcode["name"]
    return err_or_langcode
