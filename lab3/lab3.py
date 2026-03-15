import asyncio
from googletrans import Translator, LANGUAGES, LANGCODES
import sys
import time
import os

translator = Translator()

# ================= Відкриття файлу =================
file_path = "C:/Users/user/Desktop/nubip-py/lab3/Steve_Jobs.txt"
try:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    print(f"Файл: {os.path.basename(file_path)}")
except Exception as e:
    print(f"Помилка при читанні файлу: {e}")
    sys.exit()

# ================= Розбиття на речення =================
TxtList = [s.strip() for s in text.split(".") if s.strip()]
count_symbols = len(text)
count_sentence = len(TxtList)
print(f"Кількість символів: {count_symbols}")
print(f"Кількість речень: {count_sentence}")

# ================= Вибір мови перекладу =================
lang = input(
    "\nВведіть мову на яку хочете перевести\n"
    "Ви можете написати на латиниці назву мови, або код мови\n"
    "Приклад (English/english or EN/En/en): "
)

# ================= Синхронні функції =================
def LangDetect(text):
    result = translator.detect(text)
    what_lang = result.lang
    confidence = result.confidence
    result = print(f"\nМова тексту: {what_lang}; Ймовірність правильності визначення мови: {confidence}\n")
    return what_lang, confidence

def TransLate(sentence, lang):
    if lang.lower() not in LANGUAGES and lang.lower() not in LANGCODES:
        print("Помилка: Не вірна назва або код мови!")
        sys.exit()

        
    if not sentence.isdigit() and not lang.isdigit():
        result = translator.translate(text = sentence, dest = lang)
        print(f"Переклад: {result.text}\n")
        return
    elif sentence.isdigit() and lang.isdigit():
        print("Помилка: Ви намаєтесь перекласти число на число!")
        sys.exit()
    elif sentence.isdigit():
        print("Помилка: Ви намаєтесь перекласти числа!")
        sys.exit()
    elif lang.isdigit():
        print("Помилка: Мова перекладу повинна бути рядком!")
        sys.exit()

def CodeLang(lang):
    lang = lang.lower()
    if len(lang) == 2:
        full_language = LANGUAGES[lang].capitalize()
        return full_language
    else:
        code_language = LANGCODES[lang]
        return code_language

# ================= Асинхронні функції =================
async def LangDetectAsync(text):
    result = await translator.detect(text)
    what_lang = result.lang
    confidence = result.confidence
    print(f"\nМова оригінального тексту: {what_lang}; confidence: {confidence}\n")
    return what_lang, confidence

async def TransLateAsync(sentence, lang):
    if lang.lower() not in LANGUAGES and lang.lower() not in LANGCODES:
        print("Помилка: Не вірна назва або код мови!")
        return None
    try:
        result = await translator.translate(sentence, dest=lang)
        print(f"Переклад: {result.text}\n")
        return result.text
    except Exception as e:
        print(f"Помилка перекладу: {e}")
        return None

async def translate_async_all(TxtList, lang):
    tasks = [TransLateAsync(sentence, lang) for sentence in TxtList]
    translations = await asyncio.gather(*tasks)
    return translations

# ================= Основна функція =================
async def main():

    #=== sync ===

    print("\n--- Синхронний переклад ---")
    start = time.time()
    await LangDetectAsync(text)
    print("Оригінальний текст:\n")
    print(text + "\n")
    print(f"Мова перекладу: {lang.lower()}")
    for sentence in TxtList:
        await TransLateAsync(sentence, lang)
    end = time.time()
    print(f"Час виконання синхронного перекладу: {round(end - start,2)} секунд\n")

    #=== async ===

    print("\n--- Асинхронний переклад ---")
    start_async = time.time()
    await LangDetectAsync(text)
    await translate_async_all(TxtList, lang)
    end_async = time.time()
    print(f"Час виконання асинхронного перекладу: {round(end_async - start_async,2)} секунд\n")

# ================= Запуск =================
asyncio.run(main())


