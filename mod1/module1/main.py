import json
from utils import is_point_in_triangle, translate

file_name = "MyData.json"

try:
    with open(file_name, "r") as f:
        data = json.load(f)

    a, b = data["a"], data["b"]
    x, y = data["x"], data["y"]
    lang = data.get("lang", "uk")

    if lang not in ["uk", "en"]:
        lang = "uk"

    print(f"{translate('lang', lang)}")
    print(f"{translate('numbers', lang)} {a} {b}")
    print(f"{translate('coords', lang)} {x} {y}")

    if is_point_in_triangle(x, y, a, b):
        res = translate("inside", lang)
    else:
        res = translate("outside", lang)

    print(f"{translate('point', lang)} A({x}, {y}) {res} {translate('triangle_vertices', lang)} ({a},0), (0,{b}), (0,0)")

except:
    a, b = map(int, input("Введіть числа a, b: ").split())
    x, y = map(int, input("Введіть координати точки A(x,y): ").split())
    lang = input("Введіть мову інтерфейсу: ")

    data = {"a": a, "b": b, "x": x, "y": y, "lang": lang}

    with open(file_name, "w") as f:
        json.dump(data, f)

    print(f"Дані збережено в файл {file_name}")