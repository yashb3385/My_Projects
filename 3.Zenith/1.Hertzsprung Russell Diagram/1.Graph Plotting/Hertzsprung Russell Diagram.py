import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fpath = "Dataset.csv"
data = pd.read_csv(fpath)

# Renaming the columns
data.columns = [
    "Temp_K",
    "Luminosity_LLo",
    "Radius_RRo",
    "Absolute_Magnitude_Mv",
    "Star_Type",
    "Star_Color",
    "Spectral_Class"
]

# Convert to numeric values(i.e.'float' or 'int')
numeric_cols = ["Temp_K", "Luminosity_LLo", "Absolute_Magnitude_Mv"]
data[numeric_cols] = data[numeric_cols].apply(pd.to_numeric, errors="coerce")

# Dropping rows with missing values(i.e. skipping them)
data.dropna(subset=numeric_cols, inplace=True)
print(data)

# Plot HR Diagram
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x="Temp_K",
    y="Luminosity_LLo",
    hue="Star_Type",
    palette="viridis",       # For Smooth Colour Gradient
    data=data,
    s=100,                   # Dot Size
    alpha=0.8                # Transparency
)

# Invert x-axis (hotter → cooler)
plt.gca().invert_xaxis()

# Titles and labels
plt.title("Hertzsprung-Russell Diagram", fontsize=14, fontweight='bold')
plt.xlabel("Temperature (K) [Hotter → Cooler]")
plt.ylabel("Luminosity (L/Lo)")
plt.legend(title="Star Type")
plt.grid(True, linestyle="--", alpha=0.5)

# Ploting
plt.show()