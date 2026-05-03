import mysql.connector
from tabulate import tabulate

# =============================================
# конект
# =============================================

conn = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="12345",
    database="hotel",
    port=3306
)

cur = conn.cursor()

print("Підключення успішне")

# =============================================
# Вивід таблиць
# =============================================

tables = ["Guests", "Rooms", "Registration"]

for table in tables:
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()

    print(f"\nTABLE: {table}")
    print(tabulate(rows,
                   headers=[i[0] for i in cur.description],
                   tablefmt="grid"))

# =====================
# ЗАПИТ 1
# =====================
print("\n--- Номери з телевізором ---")
cur.execute("SELECT * FROM Rooms WHERE tv = 1")
print(tabulate(cur.fetchall(), headers=[i[0] for i in cur.description], tablefmt="grid"))

# =====================
# ЗАПИТ 2 (дата виїзду)
# =====================
print("\n--- Дата завершення проживання ---")
cur.execute("""
SELECT g.last_name,
       r.arrival_date,
       r.days,
       DATE_ADD(r.arrival_date, INTERVAL r.days DAY) AS end_date
FROM Registration r
JOIN Guests g ON g.guest_id = r.guest_id
""")
print(tabulate(cur.fetchall(), headers=[i[0] for i in cur.description], tablefmt="grid"))

# =====================
# ЗАПИТ 3 (кількість номерів по категоріях)
# =====================
print("\n--- Кількість номерів по категоріях ---")
cur.execute("""
SELECT category, COUNT(*) AS count_rooms
FROM Rooms
GROUP BY category
""")
print(tabulate(cur.fetchall(), headers=[i[0] for i in cur.description], tablefmt="grid"))

# =====================
# ЗАПИТ 4 (вартість проживання)
# =====================
print("\n--- Повна вартість проживання ---")
cur.execute("""
SELECT g.last_name,
       r.days,
       rm.price_per_day,
       (r.days * rm.price_per_day) AS total_price
FROM Registration r
JOIN Guests g ON g.guest_id = r.guest_id
JOIN Rooms rm ON rm.room_id = r.room_id
""")
print(tabulate(cur.fetchall(), headers=[i[0] for i in cur.description], tablefmt="grid"))

cur.close()
conn.close()