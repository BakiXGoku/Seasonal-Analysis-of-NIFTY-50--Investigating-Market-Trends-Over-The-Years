# Seasonal Analysis of NIFTY 50

## Table of Contents
- [Project Overview](#project-overview)
- [Introduction](#introduction)
- [Workflow](#workflow)
- [Results and Findings](#results-and-findings)
  - [Model Comparison](#model-comparison)
  - [Key Insights](#key-insights)
- [Files and Directories](#files-and-directories)
- [Requirements](#requirements)
- [Contributions](#contributions)
- [License](#license)
- [Final Conclusion](#final-conclusion)

## Project Overview
This project aims to analyze the seasonal patterns and trends in the NIFTY 50 index, the benchmark stock market index representing the top 50 companies listed on the National Stock Exchange (NSE) of India. Specifically, the analysis investigates:

- **Null Hypothesis (H₀):** NIFTY 50 does not exhibit seasonal patterns in Q4 (December to March) or Q1/Q2 (April to September).
- **Alternative Hypothesis (H₁):** NIFTY 50 exhibits seasonal corrections and consolidations in Q4 and rallies in Q1/Q2.

The study leverages time-series analysis techniques, such as SARIMA modeling, to validate the hypothesis using historical data from 17th September 2007 to 31st December 2024.

## Introduction
NIFTY 50, managed by NSE Indices Limited, is the most widely tracked equity benchmark in India, representing the performance of the Indian stock market. The index is calculated using the free-float market capitalization-weighted method and covers various economic sectors. Understanding seasonal behavior in the NIFTY 50 can aid investors in making informed decisions and timing their market entries and exits effectively.

## Workflow
The analysis follows a structured workflow:

0. **Data Collection**
   - Historical daily price data for the NIFTY 50 index was fetched using Yahoo Finance.

1. **Data Preprocessing**
   - Log transformation was applied to stabilize variance.
   - Differencing was performed to ensure stationarity, validated using the Augmented Dickey-Fuller (ADF) test.

2. **Exploratory Data Analysis (EDA)**
   - Seasonal patterns in Q4 (December–March) and Q1/Q2 (April–September) were visualized and compared.
   - Rolling mean and standard deviation were analyzed to confirm stationarity.

3. **Model Fitting**
   - SARIMA models were fitted separately for Q4 and Q1/Q2 data.

4. **Forecasting**
   - Forecasts were generated to predict seasonal behavior and validate against historical trends.

5. **Model Validation**
   - Metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) were computed for validation.

6. **Further Insights**
   - The observed seasonal patterns were contextualized within broader market trends, enabling actionable insights for investors.
   - refer the `results.html` for detailed insights.

## Results and Findings
### Model Comparison
#### Q4 (December–March)
- **AIC:** -7409.11
- **BIC:** -7388.14
- **Validation Metrics:**
  - MAE: 0.0118
  - MSE: 0.00029
  - RMSE: 0.0171

#### Q1/Q2 (April–September)
- **AIC:** -11632.60
- **BIC:** -11609.99
- **Validation Metrics:**
  - MAE: 0.0107
  - MSE: 0.00023
  - RMSE: 0.0153

### Key Insights
1. **Q4 Observations:** The market tends to correct and consolidate during the December–March period.
2. **Q1/Q2 Observations:** The market exhibits strong upward trends and rallies during the April–September period, aligning with the hypothesis of seasonal behavior.
3. These seasonal patterns can provide insights for investors aiming to optimize their strategies in the Indian stock market.

## Files and Directories
- **data/**: Contains the `nifty50_data.csv` file with historical data.
- **Results/**: Includes plots and visualizations.
  - `ACF_plot.png`
  - `PACF_plot.png`
  - `rolling_statistics_plot.png`
  - `Q4data_plot.png`
  - `Q1_Q2data_plot.png`
  - `forecast_plot.png`
  - `plot_diagnostics_Q4.png`
  - `plot_diagnostics_Q1_Q2.png`
  - `differenced_data_plot.png`
  - `log_transformed_data_plot.png`
  - `original_data_plot.png`
  - `results.html`
- **Scripts/**:
  - `datacollection.py`: Fetches and stores historical data.
  - `analysis.ipynb`: Performs preprocessing, EDA, model fitting, forecasting, and validation.

## Requirements
```bash
numpy==1.23.5
pandas==1.5.3
matplotlib==3.7.1
statsmodels==0.13.5
yfinance==0.2.12
```
## Contributions
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Final Conclusion
1. The analysis confirmed seasonal fluctuations in the NIFTY 50 index.
2. In Q4 (December–March), the market typically consolidates and corrects.
3. In Q1 and Q2 (April–September), the market shows upward momentum and rallies, yielding high returns.

These insights can serve as a guide for investors looking to align their strategies with the seasonal behavior of the Indian stock market.

