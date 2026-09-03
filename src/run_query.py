import sqlite3

connection = sqlite3.connect("projectile_analysis.db")

cursor = connection.cursor()

query = """
SELECT
    AVG(m.range_x) AS average_experimental_range,
    AVG(r.theoretical_range) AS average_theoretical_range,
    AVG(r.absolute_error) AS mean_absolute_error
FROM measurements AS m
JOIN model_results AS r
    ON m.trial_id = r.trial_id;
"""

cursor.execute(query)

results = cursor.fetchall()

print("Overall model performance:")

for row in results:
    print(row)

connection.close()

