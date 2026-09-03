import sqlite3

connection = sqlite3.connect("projectile_analysis.db")

cursor = connection.cursor()

tables = [
    "experiments",
    "measurements",
    "model_results"
]

print("Row counts:")

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count}")

connection.close()
