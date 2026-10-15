# Day 24: Outlier Handling Reference

## 1. Detection Methods
- **IQR (Interquartile Range)**: Robust to extreme skew, best for non-Gaussian data.
- **Z-Score**: Best when data follows an approximately Normal distribution.
- **Visual**: Boxplots and Scatter plots.

## 2. Remediation Strategies
- **Trimming / Removal**: Drop records if sample size is large and outliers are errors.
- **Winsorization / Capping**: Cap outliers at the 1st / 99th percentile or IQR boundaries.
- **Imputation**: Treat outliers as NaN and impute using median.
