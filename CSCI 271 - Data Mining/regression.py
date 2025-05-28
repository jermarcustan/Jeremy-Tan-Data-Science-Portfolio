import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression, Lasso, Ridge

# Small dataset
X = np.array([[1, 2], [2, 4], [3, 6]])  # Features (x1, x2)
y = np.array([3, 6, 9])  # Target variable

# Fit models
ols = LinearRegression().fit(X, y)
lasso = Lasso(alpha=1).fit(X, y)
ridge = Ridge(alpha=1).fit(X, y)

# Get coefficients and intercepts
ols_coef, ols_intercept = ols.coef_, ols.intercept_
lasso_coef, lasso_intercept = lasso.coef_, lasso.intercept_
ridge_coef, ridge_intercept = ridge.coef_, ridge.intercept_

# Compute predictions for training data
ols_pred_y = ols.predict(X)
lasso_pred_y = lasso.predict(X)
ridge_pred_y = ridge.predict(X)

# Compute SSE for each model
sse_ols = np.sum((y - ols_pred_y) ** 2)
sse_lasso = np.sum((y - lasso_pred_y) ** 2)
sse_ridge = np.sum((y - ridge_pred_y) ** 2)

# Print hyperplane equations and SSE values

print(f"OLS: {ols_coef[0]:.2f}X1+{ols_coef[1]:.2f}X2+{ols_intercept:.2f}")
print(f"   SSE {sse_ols:.4f}")
print(f"Lasso: {lasso_coef[0]:.2f}X1+{lasso_coef[1]:.2f}X2+{lasso_intercept:.2f}")
print(f"   SSE {sse_lasso:.4f}")
print(f"Ridge: {ridge_coef[0]:.2f}X1+{ridge_coef[1]:.2f}X2+{ridge_intercept:.2f}")
print(f"   SSE {sse_ridge:.4f}")

# Create grid for surface plot
x1_range = np.linspace(0, 4, 10)
x2_range = np.linspace(0, 8, 10)
x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)

# Compute predictions for each model
ols_pred = ols_intercept + ols_coef[0] * x1_grid + ols_coef[1] * x2_grid
lasso_pred = lasso_intercept + lasso_coef[0] * x1_grid + lasso_coef[1] * x2_grid
ridge_pred = ridge_intercept + ridge_coef[0] * x1_grid + ridge_coef[1] * x2_grid

# 3D Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot original data points
ax.scatter(X[:, 0], X[:, 1], y, color='black', label="Data Points", s=50)

# Plot regression planes with colormaps
ax.plot_surface(x1_grid, x2_grid, ols_pred, alpha=0.5, cmap='Blues', edgecolor='none')
ax.plot_surface(x1_grid, x2_grid, lasso_pred, alpha=0.5, cmap='Reds', edgecolor='none')
ax.plot_surface(x1_grid, x2_grid, ridge_pred, alpha=0.5, cmap='Greens', edgecolor='none')

# Labels
ax.set_xlabel("X1")
ax.set_ylabel("X2")
ax.set_zlabel("Y")
ax.set_title("Regression Planes: OLS vs. Lasso vs. Ridge")

# Show plot
plt.show()


