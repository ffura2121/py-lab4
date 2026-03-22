import json, os
from modules import mod_gtrans4 as m
import asyncio

async def main():
    with open("config.json") as f:
        cfg = json.load(f)

    file = cfg["file"]

    if not os.path.exists(file):
        print("file error")
        return

    text = open(file, encoding="utf-8").read()
    sentences = text.split(".")[:cfg["sentences"]]

    translated = []
    for s in sentences:
        translated.append(await m.TransLate(s, "auto", cfg["dest"]))

    if cfg["output"] == "file":
        open(file + "_" + cfg["dest"], "w").write("\n".join(translated))
        print("Ok")
    else:
        print("\n".join(translated))

asyncio.run(main())