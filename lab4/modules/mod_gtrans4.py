from googletrans import Translator, LANGUAGES, LANGCODES

translator = Translator()

async def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        result = await translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return str(e)

async def LangDetect(text: str, set: str = "all") -> str:
    try:
        res = await translator.detect(text)
        if set == "lang":
            return res.lang
        elif set == "confidence":
            return str(res.confidence)
        return f"{res.lang} ({res.confidence})"
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang]
    elif lang in LANGCODES:
        return LANGCODES[lang]
    return "error"

async def LanguageList(out="screen", text=None):
    try:
        result = []
        for code, name in LANGUAGES.items():
            row = f"{code:<10} {name:<20}"
            if text:
                tr = await translator.translate(text, dest=code)
                row += f" | {tr.text}"
            result.append(row)

        if out == "file":
            with open("langs.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(result))
        else:
            print("\n".join(result))

        return "Ok"
    except Exception as e:
        return str(e)