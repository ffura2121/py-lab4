# Використовуємо Python 3.11
FROM python:3.11

# Робоча директорія всередині контейнера
WORKDIR /kosenko

# Копіюємо весь проєкт у контейнер
COPY . .

# Встановлюємо пакети, сумісні з Python ≤3.12
RUN pip install googletrans==3.1.0a0

# Команда запуску скрипту з модулем для Python ≤3.12
CMD ["python", "gtrans3.py"]