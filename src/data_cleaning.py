import pandas as pd

df = pd.read_csv("data/raw/projectile_experiment.csv")

print(df.head())

print("\nDataset information:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nInvalid launch angles:")
print(df[(df["launch_angle"] < 0) | (df["launch_angle"] > 90)])

print("\nInvalid initial velocities:")
print(df[df["initial_velocity"] <= 0])

print("\nInvalid flight times:")
print(df[df["flight_time"] <= 0])

print("\nInvalid ranges:")
print(df[df["range_x"] < 0])

print("\nInvalid maximum heights:")
print(df[df["max_height"] < 0])

print("\nDuplicate trial IDs:")
print(df["trial_id"].duplicated().sum())

output_path = "data/processed/projectile_clean.csv"

df.to_csv(output_path, index=False)

print(f"\nCleaned dataset saved to: {output_path}")
