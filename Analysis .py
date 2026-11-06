import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 1. Load the CSV file (Using the correct raw GitHub URL)
file_path = 'https://raw.githubusercontent.com/Maduagwuna-tech/nigeria-fdi-economic-growth/d308c29334e1837913e5cb0ebb4404e076acccad/nigeria_fdi_gdp_1990_2024.csv'
df = pd.read_csv(file_path)

# Display dataset basic info and summary statistics
print("--- Data Head ---")
print(df.head())
print("\n--- Summary Statistics ---")
print(df.describe())

# 2. Prepare Variables for Regression
# Y: GDP Growth (Dependent Variable)
# X: FDI Net Inflows (Independent Variable)
Y = df['GDP_Growth']
X = df['FDI_Net_Inflows']

# Add constant to calculate beta_0 (intercept)
X_const = sm.add_constant(X)

# 3. Fit OLS Model
model = sm.OLS(Y, X_const).fit()

# Print Regression Results
print("\n" + "="*50)
print("OLS REGRESSION RESULTS")
print("="*50)
print(model.summary())

# Extract key statistics
beta_0 = model.params['const']
beta_1 = model.params['FDI_Net_Inflows']
p_value = model.pvalues['FDI_Net_Inflows']
r_squared = model.rsquared

print("\n--- Hypothesis Test Conclusion ---")
print(f"Regression Equation: GDP_Growth = {beta_0:.4f} + {beta_1:.4f} * FDI_Net_Inflows")
print(f"R-squared: {r_squared:.4f}")
print(f"p-value for FDI: {p_value:.4f}")

if p_value < 0.05:
    print("Decision: Reject H0 at alpha = 0.05 level.")
    print("Conclusion: FDI net inflows have a statistically significant relationship with GDP growth in Nigeria (1990–2024).")
else:
    print("Decision: Fail to reject H0 at alpha = 0.05 level.")
    print("Conclusion: FDI net inflows do not have a statistically significant relationship with GDP growth in Nigeria (1990–2024).")

# 4. Data Visualizations
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Regression Line & Scatter Plot
axes[0].scatter(df['FDI_Net_Inflows'], df['GDP_Growth'], color='blue', alpha=0.7, label='Actual Data')
x_vals = np.linspace(df['FDI_Net_Inflows'].min(), df['FDI_Net_Inflows'].max(), 100)
y_vals = beta_0 + beta_1 * x_vals
axes[0].plot(x_vals, y_vals, color='red', linewidth=2, label=f'Fit: Y = {beta_0:.2f} + {beta_1:.2f}X')
axes[0].set_xlabel('FDI Net Inflows (% of GDP)')
axes[0].set_ylabel('GDP Growth (Annual %)')
axes[0].set_title('FDI vs. GDP Growth in Nigeria (1990–2024)')
axes[0].grid(True, linestyle='--', alpha=0.5)
axes[0].legend()

# Plot 2: Time Series Overlay
axes[1].plot(df['Year'], df['GDP_Growth'], label='GDP Growth (%)', color='green', marker='o')
axes[1].plot(df['Year'], df['FDI_Net_Inflows'], label='FDI Net Inflows (% of GDP)', color='orange', marker='s')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Percentage (%)')
axes[1].set_title('Trends of GDP Growth and FDI Net Inflows (1990–2024)')
axes[1].grid(True, linestyle='--', alpha=0.5)
axes[1].legend()

plt.tight_layout()
plt.savefig('nigeria_fdi_gdp_regression_plot.png', dpi=300)
plt.show()