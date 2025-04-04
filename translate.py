import json

from colorama import Fore, init

from graph import stream_graph_updates
from langdetect_lab import detect_language

init(autoreset=True)


def translate_question(question: str, source: str, target: str = "Svenska"):
    question = f"Convert this question: {question}, from SOURCE LANGUAGE {source} to TARGET LANGUAGE {target}"
    print(f"Translation prompt: {Fore.LIGHTMAGENTA_EX + question}")
    translated = stream_graph_updates(user_input=question)
    return translated


if __name__ == "__main__":
    with open("languages.json") as fp:
        questions = json.load(fp)

    for item in questions["questions"]:
        for language, question in item.items():
            lang = detect_language(question)
            translated_question = translate_question(question, source=lang)
            print(f"input question: {Fore.RED + question}")
            print(f"translated question: {Fore.GREEN + translated_question}\n")
