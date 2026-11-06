# Nigeria: Foreign Direct Investment (FDI) and Economic Growth Analysis (1990–2024)

An econometric analysis exploring the relationship between **Foreign Direct Investment (FDI) net inflows (% of GDP)** and **Annual GDP Growth (%)** in Nigeria from 1990 to 2024 using Ordinary Least Squares (OLS) regression.

---

##  Research Overview

* **Research Question:** Does Foreign Direct Investment have a statistically significant relationship with economic growth in Nigeria?
* **Data Sources:** World Development Indicators (WDI), The World Bank
  * **Dependent Variable (Y):** GDP growth (annual %) [Indicator: `NY.GDP.MKTP.KD.ZG`]
  * **Independent Variable (X):** FDI net inflows (% of GDP) [Indicator: `BX.KLT.DINV.WD.GD.ZS`]
* **Sample Period:** 1990–2024 (N = 35 observations)

---

##  Hypotheses

* **Null Hypothesis (H₀):** FDI has no statistically significant relationship with economic growth in Nigeria.
* **Alternative Hypothesis (H₁):** FDI has a statistically significant relationship with economic growth in Nigeria.

---

##  Regression Model & Results

**Model Equation:**
> **GDP_Growth**<sub>t</sub> = β₀ + β₁ **FDI_Net_Inflows**<sub>t</sub> + ε<sub>t</sub>

### Key Statistical Findings:
* **Fitted Equation:** GDP_Growth = 1.9641 + 1.6820 × FDI_Net_Inflows
* **R²:** `0.1200` (Adjusted R²: `0.0930`)
* **F-statistic:** `4.487` (p-value = `0.0418`)
* **FDI Coefficient p-value:** `0.042` (< 0.05)

### Conclusion:
Since the p-value (0.042) is below the standard 0.05 significance threshold, we **reject the null hypothesis (H₀)**. The analysis indicates a statistically significant positive relationship between FDI net inflows and annual GDP growth in Nigeria over the 1990–2024 period.

---

##  Repository Structure

```text
├── nigeria_fdi_gdp_1990_2024.csv    # Cleaned and combined World Bank dataset
├── analysis.py                     # Python script for OLS regression & plots
├── nigeria_fdi_gdp_regression_plot.png # Visualizations (Scatter fit & Time series)
└── README.md                       # Project documentation
