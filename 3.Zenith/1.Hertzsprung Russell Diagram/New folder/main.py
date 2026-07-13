import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Data Loading and Cleaning
df = pd.read_csv('Dataset.csv')

# Renaming columns for easier access
df.columns = ['Temperature', 'Luminosity', 'Radius', 'Magnitude', 'Star_type', 'Star_color', 'Spectral_Class']

# 2. Exploratory Analysis & Feature Engineering
# Create Log-Transformed Features
df['log_Temperature'] = np.log10(df['Temperature'])
df['log_Luminosity'] = np.log10(df['Luminosity'])
df['log_Radius'] = np.log10(df['Radius'])

# Correlation Matrix
plt.figure(figsize=(10, 8))
sns.heatmap(df[['Temperature', 'Luminosity', 'Radius', 'Magnitude', 
                'log_Temperature', 'log_Luminosity', 'log_Radius']].corr(), 
            annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix: Raw vs Log Features")
plt.tight_layout()
plt.savefig('correlation_matrix.png')
plt.close()

# 3. Data Preparation
# We will compare models using Raw features vs Log features
# Set 1: Raw Features (for Poly Regression & Random Forest)
X_raw = df[['Temperature', 'Luminosity', 'Radius']]
y = df['Magnitude']

# Set 2: Log Features (for Linear Regression)
X_log = df[['log_Temperature', 'log_Luminosity', 'log_Radius']]

# Split Data (80% Train, 20% Test)
X_train_raw, X_test_raw, y_train, y_test = train_test_split(X_raw, y, test_size=0.2, random_state=42)
X_train_log, X_test_log, _, _ = train_test_split(X_log, y, test_size=0.2, random_state=42)

# Normalization (Min-Max Scaling)
scaler_raw = MinMaxScaler()
X_train_raw_scaled = scaler_raw.fit_transform(X_train_raw)
X_test_raw_scaled = scaler_raw.transform(X_test_raw)

scaler_log = MinMaxScaler()
X_train_log_scaled = scaler_log.fit_transform(X_train_log)
X_test_log_scaled = scaler_log.transform(X_test_log)

# 4. Model Training

# Model A: Linear Regression (Using Log Features)
# Linear regression works best when relationships are linear (which they are in Log space)
lr_model = LinearRegression()
lr_model.fit(X_train_log_scaled, y_train)
y_pred_lr = lr_model.predict(X_test_log_scaled)

# Model B: Polynomial Regression (Degree 2, Using Raw Features)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train_raw_scaled)
X_test_poly = poly.transform(X_test_raw_scaled)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
y_pred_poly = poly_model.predict(X_test_poly)

# Model C: Random Forest Regressor (Using Raw Features)
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train_raw_scaled, y_train)
y_pred_rf = rf_model.predict(X_test_raw_scaled)

# 5. Model Evaluation
models = {
    "Linear Regression (Log Features)": y_pred_lr,
    "Polynomial Regression (Raw Features)": y_pred_poly,
    "Random Forest (Raw Features)": y_pred_rf
}

print(f"{'Model':<40} | {'MSE':<10} | {'RMSE':<10} | {'R2 Score':<10}")
print("-" * 80)

for name, y_pred in models.items():
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    print(f"{name:<40} | {mse:<10.4f} | {rmse:<10.4f} | {r2:<10.4f}")

# 6. Visualization of Results (Predicted vs Actual)
plt.figure(figsize=(18, 5))

for i, (name, y_pred) in enumerate(models.items()):
    plt.subplot(1, 3, i+1)
    plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2) # Identity line
    plt.xlabel('Actual Magnitude')
    plt.ylabel('Predicted Magnitude')
    plt.title(f'{name}\nR2: {r2_score(y_test, y_pred):.2f}')

plt.tight_layout()
plt.savefig('predicted_vs_actual.png')
plt.show()