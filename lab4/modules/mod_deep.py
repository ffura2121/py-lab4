from deep_translator import GoogleTranslator
from langdetect import detect

def TransLate(text, scr, dest):
    try:
        return GoogleTranslator(source=scr, target=dest).translate(text)
    except Exception as e:
        return str(e)

def LangDetect(text, set="all"):
    lang = detect(text)
    if set == "lang":
        return lang
    return f"{lang} (1.0)"

def CodeLang(lang):
    return lang

def LanguageList(out="screen", text=None):
    langs = ["en","uk","fr","de"]
    result = []
    for l in langs:
        row = l
        if text:
            row += " | " + TransLate(text, "auto", l)
        result.append(row)

    if out == "file":
        open("langs.txt","w").write("\n".join(result))
    else:
        print("\n".join(result))

    return "Ok"