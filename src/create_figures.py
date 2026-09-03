import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the model results
df = pd.read_csv("data/processed/model_results.csv")

# Calculate average values by launch angle
grouped = df.groupby("launch_angle").agg({
    "range_x": "mean",
    "theoretical_range": "mean"
}).reset_index()

# Create the plot
plt.figure(figsize=(10, 6))

plt.plot(
    grouped["launch_angle"],
    grouped["range_x"],
    marker="o",
    label="Experimental Range"
)

plt.plot(
    grouped["launch_angle"],
    grouped["theoretical_range"],
    marker="o",
    label="Theoretical Range"
)

plt.xlabel("Launch Angle (degrees)")
plt.ylabel("Range (m)")
plt.title("Experimental vs. Theoretical Range by Launch Angle")
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig("figures/range_vs_angle.png", dpi=300, bbox_inches="tight")

plt.show()

print("Figure saved to figures/range_vs_angle.png")

# Calculate average absolute error by launch angle
error_by_angle = (
    df.groupby("launch_angle")["absolute_error"]
    .mean()
    .reset_index()
)

# Create the plot
plt.figure(figsize=(10, 6))

plt.bar(
    error_by_angle["launch_angle"],
    error_by_angle["absolute_error"],
    width=3
)

plt.xlabel("Launch Angle (degrees)")
plt.ylabel("Mean Absolute Error (m)")
plt.title("Average Absolute Error by Launch Angle")
plt.grid(axis="y", alpha=0.3)

# Save the figure
plt.savefig(
    "figures/error_by_angle.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Figure saved to figures/error_by_angle.png")

# Create residual plot
plt.figure(figsize=(10, 6))

plt.scatter(
    df["launch_angle"],
    df["residual"]
)

# Add zero reference line
plt.axhline(
    y=0,
    linestyle="--"
)

plt.xlabel("Launch Angle (degrees)")
plt.ylabel("Residual (m)")
plt.title("Residuals by Launch Angle")
plt.grid(True, alpha=0.3)

# Save the figure
plt.savefig(
    "figures/residuals.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Figure saved to figures/residuals.png")

# Load regression model comparison results
model_comparison = pd.read_csv(
    "data/processed/regression_model_comparison.csv"
)

# Create R² comparison plot
plt.figure(figsize=(10, 6))

plt.bar(
    model_comparison["Model"],
    model_comparison["R2"]
)

plt.xlabel("Regression Model")
plt.ylabel("R²")
plt.title("Regression Model Performance Comparison")
plt.xticks(rotation=15)
plt.ylim(0, 1.05)
plt.grid(axis="y", alpha=0.3)

# Save the figure
plt.savefig(
    "figures/model_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Figure saved to figures/model_comparison.png")
