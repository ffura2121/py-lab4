import asyncio
from modules import mod_gtrans4 as m

async def main():
    text = "Hello world"
    print(await m.TransLate(text, "auto", "uk"))
    print(await m.LangDetect(text))
    print(m.CodeLang("en"))

asyncio.run(main())