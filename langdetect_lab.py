# https://github.com/Mimino666/langdetect
# $ pip install langdetect
# "This library is a direct port of Google's language-detection library from Java to Python. All the classes and
# methods are unchanged, so for more information see the project's website or wiki."
# Possible limitation: currently only supports 55 languages.

import json

from colorama import Fore, init
from langdetect import detect

from langcodes import get_language_name

init(autoreset=True)


def detect_language(question: str):
    detection = detect(question)
    if "not found" in (lang := get_language_name(detection)):
        raise Exception("language not detected")
    print(f"Language detection: {Fore.CYAN + lang}")
    return lang


if __name__ == "__main__":
    with open("languages.json") as fp:
        questions = json.load(fp)

    for question in questions["questions"]:
        print(f"question object: {question}")
        for k, v in question.items():
            print(f"\nLanguage: {k}, Question: {v}")
            detection = detect(v)
            print(f"Detection {detection}")
            print(f"Langcode to lang: {Fore.GREEN + get_language_name(detection)}")
