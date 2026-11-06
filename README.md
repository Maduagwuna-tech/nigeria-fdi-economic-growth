# Foreign Direct Investment and Economic Growth in Nigeria (1990–2024)

## Project Overview
This project investigates the relationship between Foreign Direct Investment (FDI) and Economic Growth in Nigeria using World Bank data from 1990 to 2024. A simple Ordinary Least Squares (OLS) linear regression model was built in Python to evaluate the impact of FDI on annual GDP growth.

---

## Key Findings & Results
- **Sample Size (N):** 35 annual observations (1990–2024)
- **Regression Equation:** GDP Growth = 1.9641 + 1.6820 * (FDI Net Inflows)
- **Slope:** 1.6820 (p = 0.042) — A 1% increase in FDI net inflows is associated with a 1.68% increase in annual GDP growth.
- **Statistical Significance:** Because the p-value (0.042) is less than 0.05, we reject the null hypothesis and conclude there is a statistically significant positive relationship.
- **Model Fit:** R-squared = 0.120 — FDI explains about 12% of the variation in Nigeria's GDP growth over this period.

---

## Repository Contents
- `nigeria_fdi_gdp_1990_2024.csv`: The cleaned dataset used for analysis.
- `nigeria_fdi_regression_analysis.py`: The Python script used to process data and run the OLS regression.
- `nigeria_fdi_gdp_regression.png`: Scatter plot visualization of the regression trendline.

---

## How to Run the Code
1. Clone or download this repository.
2. Install the required Python packages:
   ```bash
   pip install pandas statsmodels matplotlib seaborn
