import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

try:
    df = pd.read_csv("lab7/employees.csv")
    print("Ok")
except:
    print("Помилка відкриття CSV")
    exit()

def age(date):
    birth = datetime.strptime(date, "%d.%m.%Y")
    today = datetime.today()
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

df["Вік"] = df["Дата народження"].apply(age)

# Стать
gender = df["Стать"].value_counts()
print(gender)

gender.plot(kind="pie", autopct="%1.1f%%")
plt.title("Стать")
plt.ylabel("")
plt.show()

# Вікові групи
groups = {
    "younger_18": len(df[df["Вік"] < 18]),
    "18-45": len(df[(df["Вік"] >= 18) & (df["Вік"] < 45)]),
    "45-70": len(df[(df["Вік"] >= 45) & (df["Вік"] < 70)]),
    "older_70": len(df[df["Вік"] >= 70])
}

print(groups)

plt.bar(groups.keys(), groups.values())
plt.title("Вікові категорії")
plt.show()

# Стать + вік
for g in groups.keys():
    if g == "younger_18":
        temp = df[df["Вік"] < 18]
    elif g == "18-45":
        temp = df[(df["Вік"] >= 18) & (df["Вік"] < 45)]
    elif g == "45-70":
        temp = df[(df["Вік"] >= 45) & (df["Вік"] < 70)]
    else:
        temp = df[df["Вік"] >= 70]

    data = temp["Стать"].value_counts()
    print(g)
    print(data)

    data.plot(kind="bar")
    plt.title(g)
    plt.show()