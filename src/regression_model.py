import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the model results
df = pd.read_csv("data/processed/model_results.csv")

print(df.head())

# Define input variables
X = df[["initial_velocity", "launch_angle"]]

# Define the target variable
y = df["range_x"]

print("\nInput variables:")
print(X.head())

print("\nTarget variable:")
print(y.head())

# Create the linear regression model
model = LinearRegression()

# Train the model using our experimental data
model.fit(X, y)

print("\nRegression model trained successfully!")

# Display the regression coefficients

print("\nRegression coefficients:")
print(f"Intercept: {model.intercept_:.4f}")
print(f"Initial velocity coefficient: {model.coef_[0]:.4f}")
print(f"Launch angle coefficient: {model.coef_[1]:.4f}")

# Generate predictions using the regression model

df["predicted_range"] = model.predict(X)

print("\nExperimental vs. predicted range:")
print(
    df[
        [
            "trial_id",
            "initial_velocity",
            "launch_angle",
            "range_x",
            "predicted_range"
        ]
    ].head(10)
)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Calculate regression performance metrics

r2 = r2_score(y, df["predicted_range"])
mae = mean_absolute_error(y, df["predicted_range"])
rmse = np.sqrt(mean_squared_error(y, df["predicted_range"]))

print("\nLinear regression performance:")
print(f"R²: {r2:.4f}")
print(f"MAE: {mae:.4f} m")
print(f"RMSE: {rmse:.4f} m")

# Create physics-informed features

df["velocity_squared"] = df["initial_velocity"] ** 2

angle_radians = np.radians(df["launch_angle"])

df["sin_2theta"] = np.sin(2 * angle_radians)

print("\nPhysics-informed features:")
print(
    df[
        [
            "initial_velocity",
            "launch_angle",
            "velocity_squared",
            "sin_2theta"
        ]
    ].head()
)

# Define physics-informed input variables
X_physics = df[["velocity_squared", "sin_2theta"]]

# Define the target
y = df["range_x"]

# Create and train the regression model
physics_regression = LinearRegression()

physics_regression.fit(X_physics, y)

print("\nPhysics-informed regression model trained successfully!")

# Generate predictions
df["physics_predicted_range"] = physics_regression.predict(X_physics)

# Calculate performance metrics
physics_r2 = r2_score(y, df["physics_predicted_range"])
physics_mae = mean_absolute_error(y, df["physics_predicted_range"])
physics_rmse = np.sqrt(
    mean_squared_error(y, df["physics_predicted_range"])
)

print("\nPhysics-informed regression performance:")
print(f"R²: {physics_r2:.4f}")
print(f"MAE: {physics_mae:.4f} m")
print(f"RMSE: {physics_rmse:.4f} m")

# Create an interaction feature that matches the physics equation
df["physics_term"] = (
    df["velocity_squared"] * df["sin_2theta"]
)

print("\nPhysics interaction feature:")
print(
    df[
        [
            "velocity_squared",
            "sin_2theta",
            "physics_term"
        ]
    ].head()
)

# Use the physics interaction term as the regression input
X_interaction = df[["physics_term"]]

# Target variable
y = df["range_x"]

# Create and train the interaction regression model
interaction_regression = LinearRegression()

interaction_regression.fit(X_interaction, y)

print("\nInteraction regression model trained successfully!")

# Generate predictions
df["interaction_predicted_range"] = (
    interaction_regression.predict(X_interaction)
)

# Evaluate the model
interaction_r2 = r2_score(
    y,
    df["interaction_predicted_range"]
)

interaction_mae = mean_absolute_error(
    y,
    df["interaction_predicted_range"]
)

interaction_rmse = np.sqrt(
    mean_squared_error(
        y,
        df["interaction_predicted_range"]
    )
)

print("\nInteraction regression performance:")
print(f"R²: {interaction_r2:.4f}")
print(f"MAE: {interaction_mae:.4f} m")
print(f"RMSE: {interaction_rmse:.4f} m")

# Create a summary of regression model performance
model_comparison = pd.DataFrame({
    "Model": [
        "Basic Linear Regression",
        "Physics-Informed Regression",
        "Interaction Regression"
    ],
    "R2": [
        r2,
        physics_r2,
        interaction_r2
    ],
    "MAE_m": [
        mae,
        physics_mae,
        interaction_mae
    ],
    "RMSE_m": [
        rmse,
        physics_rmse,
        interaction_rmse
    ]
})

print("\nModel Comparison:")
print(model_comparison)

# Save model comparison results
model_comparison.to_csv(
    "data/processed/regression_model_comparison.csv",
    index=False
)

print(
    "\nModel comparison saved to: "
    "data/processed/regression_model_comparison.csv"
)
