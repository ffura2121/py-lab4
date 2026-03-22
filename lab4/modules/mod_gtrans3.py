from googletrans import Translator, LANGUAGES, LANGCODES
import sys

if sys.version_info >= (3, 13):
    raise Exception("Python >=3.13 не підтримується")

translator = Translator()

def TransLate(text, scr, dest):
    try:
        return translator.translate(text, src=scr, dest=dest).text
    except Exception as e:
        return str(e)

def LangDetect(text, set="all"):
    res = translator.detect(text)
    if set == "lang":
        return res.lang
    elif set == "confidence":
        return str(res.confidence)
    return f"{res.lang} ({res.confidence})"

def CodeLang(lang):
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang]
    elif lang in LANGCODES:
        return LANGCODES[lang]
    return "error"

def LanguageList(out="screen", text=None):
    result = []
    for code, name in LANGUAGES.items():
        row = f"{code:<10} {name:<20}"
        if text:
            tr = translator.translate(text, dest=code)
            row += f" | {tr.text}"
        result.append(row)

    if out == "file":
        open("langs.txt","w",encoding="utf-8").write("\n".join(result))
    else:
        print("\n".join(result))

    return "Ok"