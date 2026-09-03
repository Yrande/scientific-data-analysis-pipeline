import sqlite3
import pandas as pd

# Load the processed dataset
df = pd.read_csv("data/processed/model_results.csv")

# Connect to the SQLite database
connection = sqlite3.connect("projectile_analysis.db")

# Insert experiment information
df[
    ["trial_id", "launch_angle", "initial_velocity"]
].to_sql(
    "experiments",
    connection,
    if_exists="append",
    index=False
)

# Insert measurement information
df[
    ["trial_id", "flight_time", "range_x", "max_height"]
].to_sql(
    "measurements",
    connection,
    if_exists="append",
    index=False
)

# Insert model results
df[
    [
        "trial_id",
        "theoretical_range",
        "residual",
        "absolute_error",
        "percent_error"
    ]
].to_sql(
    "model_results",
    connection,
    if_exists="append",
    index=False
)

# Save changes
connection.commit()

# Close database
connection.close()

print("Data loaded successfully!")
print(f"Total trials loaded: {len(df)}")
