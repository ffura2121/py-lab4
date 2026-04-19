import re
import os

ukr = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

def sort_key(word):
    first = word[0].lower()

    if first in ukr:
        group = 0
    elif first.isalpha():
        group = 1
    else:
        group = 2

    return (group, word.lower())

path = os.path.join(os.path.dirname(__file__), "text.txt")
with open(path, "r", encoding="utf-8") as file:
    text = file.read()

print("Початковий текст:\n")
print(text)

words = re.findall(r"[A-Za-zА-Яа-яІіЇїЄєҐґ'-]+", text)

sorted_words = sorted(words, key=sort_key)

print("\nВідсортовані слова:\n")
print(sorted_words)