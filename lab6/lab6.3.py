import json

data = {
    "Косенко": ["Іван", "Олегович", 2005],
    "Шевченко": ["Тарас", "Григорович", 1814],
    "Бондар": ["Олена", "Іванівна", 2001],
    "Мельник": ["Андрій", "Петрович", 1999],
    "Ткаченко": ["Марія", "Олександрівна", 2000],
    "Коваленко": ["Ігор", "Сергійович", 1998],
    "Петренко": ["Наталія", "Юріївна", 2002],
    "Іваненко": ["Дмитро", "Васильович", 2003],
    "Савченко": ["Оксана", "Миколаївна", 2004],
    "Романюк": ["Віктор", "Степанович", 1997]
}

with open("people.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

with open("people.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

print("Дані з JSON:\n")

for surname, info in loaded.items():
    print(surname, info)