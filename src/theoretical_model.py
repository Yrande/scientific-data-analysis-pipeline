print("Theoretical model script is running!")

import pandas as pd
import numpy as np

# Load the cleaned experimental data
df = pd.read_csv("data/processed/projectile_clean.csv")

# Gravitational acceleration
g = 9.81

# Convert launch angle from degrees to radians
angle_radians = np.radians(df["launch_angle"])

# Calculate theoretical range
df["theoretical_range"] = (
    df["initial_velocity"] ** 2
    * np.sin(2 * angle_radians)
    / g
)

# Display the results
print(df[
    [
        "trial_id",
        "launch_angle",
        "initial_velocity",
        "range_x",
        "theoretical_range"
    ]
].head(10))

# Calculate residual
df["residual"] = df["range_x"] - df["theoretical_range"]

# Calculate absolute error
df["absolute_error"] = abs(df["range_x"] - df["theoretical_range"])

# Calculate percent error
df["percent_error"] = (
    df["absolute_error"] / df["theoretical_range"]
) * 100

print("\nExperimental vs theoretical results:")
print(df[
    [
        "trial_id",
        "launch_angle",
        "range_x",
        "theoretical_range",
        "residual",
        "absolute_error",
        "percent_error"
    ]
].head(10))

# Calculate Mean Absolute Error
mae = df["absolute_error"].mean()

print("\nModel accuracy:")
print(f"Mean Absolute Error (MAE): {mae:.4f} m")

# Calculate Root Mean Squared Error
rmse = np.sqrt((df["residual"] ** 2).mean())

print(f"Root Mean Squared Error (RMSE): {rmse:.4f} m")

# Calculate average error by launch angle
error_by_angle = df.groupby("launch_angle")["absolute_error"].mean()

print("\nAverage absolute error by launch angle:")
print(error_by_angle)

import matplotlib.pyplot as plt

# Plot average absolute error by launch angle
error_by_angle.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Average Absolute Error by Launch Angle")
plt.xlabel("Launch Angle (degrees)")
plt.ylabel("Average Absolute Error (m)")
plt.tight_layout()

plt.show()

# Calculate average experimental range by launch angle
range_by_angle = df.groupby("launch_angle")["range_x"].mean()

print("\nAverage experimental range by launch angle:")
print(range_by_angle)

# Plot average experimental range by launch angle

range_by_angle.plot(
    kind="line",
    marker="o",
    figsize=(10, 6)
)

plt.title("Average Experimental Range by Launch Angle")
plt.xlabel("Launch Angle (degrees)")
plt.ylabel("Average Experimental Range (m)")
plt.grid(True)
plt.tight_layout()

plt.show()

# Calculate average theoretical range by launch angle
theoretical_by_angle = df.groupby("launch_angle")["theoretical_range"].mean()

# Plot experimental and theoretical range
plt.figure(figsize=(10, 6))

plt.plot(
    range_by_angle.index,
    range_by_angle.values,
    marker="o",
    label="Experimental"
)

plt.plot(
    theoretical_by_angle.index,
    theoretical_by_angle.values,
    marker="o",
    label="Theoretical"
)

plt.title("Experimental vs. Theoretical Projectile Range")
plt.xlabel("Launch Angle (degrees)")
plt.ylabel("Average Range (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

# Plot residuals by launch angle

plt.figure(figsize=(10, 6))

plt.scatter(
    df["launch_angle"],
    df["residual"]
)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.title("Residuals by Launch Angle")
plt.xlabel("Launch Angle (degrees)")
plt.ylabel("Residual (m)")
plt.grid(True)
plt.tight_layout()

plt.show()

# Statistical summary of experimental range

mean_range = df["range_x"].mean()
std_range = df["range_x"].std()
standard_error = std_range / np.sqrt(len(df))

print("\nStatistical summary of experimental range:")
print(f"Mean range: {mean_range:.4f} m")
print(f"Standard deviation: {std_range:.4f} m")
print(f"Standard error: {standard_error:.4f} m")

# Statistical summary by launch angle

stats_by_angle = df.groupby("launch_angle")["range_x"].agg(
    ["mean", "std", "count"]
)

stats_by_angle["standard_error"] = (
    stats_by_angle["std"] / np.sqrt(stats_by_angle["count"])
)

print("\nStatistical summary by launch angle:")
print(stats_by_angle)

# Compare experimental and theoretical range by launch angle

comparison = df.groupby("launch_angle")[["range_x", "theoretical_range"]].mean()

comparison.plot(
    kind="line",
    marker="o",
    figsize=(10, 6)
)

plt.title("Experimental vs. Theoretical Projectile Range")
plt.xlabel("Launch Angle (degrees)")
plt.ylabel("Range (m)")
plt.legend(["Experimental", "Theoretical"])
plt.grid(True)

plt.tight_layout()
plt.show()

# Save model results

output_path = "data/processed/model_results.csv"

df.to_csv(output_path, index=False)

print(f"\nModel results saved to: {output_path}")
