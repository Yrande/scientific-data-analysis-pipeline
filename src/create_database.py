import sqlite3

# Create/connect to the SQLite database
connection = sqlite3.connect("projectile_analysis.db")

# Create a cursor
cursor = connection.cursor()

# Read the SQL table definitions
with open("sql/create_tables.sql", "r") as file:
    sql_script = file.read()

# Execute the SQL script
cursor.executescript(sql_script)

# Save the changes
connection.commit()

# Close the database connection
connection.close()

print("Database created successfully!")
