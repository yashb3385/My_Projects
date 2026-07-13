import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
import numpy as np

print("---------------------------------------------------------------------------------------------------------------------------------\n\n")

# Load the dataset & rename columns for accessibility
df = pd.read_csv('Dataset.csv')
df.columns = ['Temperature', 'Luminosity', 'Radius', 'Absolute_magnitude', 'Star_type', 'Star_color', 'Spectral_class']

# Improved Preprocessing: Convert only numeric columns to numeric types
numeric_cols = ['Temperature', 'Luminosity', 'Radius', 'Absolute_magnitude', 'Star_type']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Dropping rows with missing values in the features of interest
df.dropna(subset=['Temperature', 'Absolute_magnitude'], inplace=True)

print("Data Loaded and Cleaned.\n")

# Select features for HR diagram (Temperature & Absolute Magnitude)
features = df[['Temperature', 'Absolute_magnitude']]

# Scale the features (K-Means is sensitive to the scale of data)
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

print("################################################################################################################################\n\n")
print("CALCULATING ELBOW METHOD...\n")

# 1. Elbow Method Implementation
wcss = []
k_range = range(1, 11)  # Test k from 1 to 10

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(features_scaled)
    wcss.append(kmeans.inertia_)

# 2. Find the Optimal K programmatically (Distance to Line Method)
# This finds the point with the maximum distance to the line connecting the first and last points
p1 = np.array([k_range[0], wcss[0]])
p2 = np.array([k_range[-1], wcss[-1]])

distances = []
for i in range(len(k_range)):
    p = np.array([k_range[i], wcss[i]])
    # Perpendicular distance formula
    d = np.abs(np.cross(p2-p1, p1-p)) / np.linalg.norm(p2-p1)
    distances.append(d)

optimal_k = k_range[np.argmax(distances)]
print(f"✅ Optimal k determined by Elbow Method: {optimal_k}\n")

# 3. Plot Elbow Graph
plt.figure(figsize=(10, 6))
plt.plot(k_range, wcss, marker='o', linestyle='--', color='b')
plt.axvline(x=optimal_k, color='r', linestyle='--', label=f'Optimal k = {optimal_k}')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS (Inertia)')
plt.legend()
plt.grid(True)
plt.savefig('Elbow_Estimation_Graph.png')
plt.show()

print("################################################################################################################################\n\n")

# 4. Perform Clustering with the Optimal k
# (You can add more values to this list if you want to compare, e.g., ks = [optimal_k, 4, 5])
ks = [optimal_k]

fig, axes = plt.subplots(1, len(ks), figsize=(10 * len(ks), 6))
if len(ks) == 1: axes = [axes]  # Ensure axes is iterable if single plot

for i, k in enumerate(ks):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(features_scaled)
    df[f'Cluster_{k}'] = clusters
    centroids_scaled = kmeans.cluster_centers_

    # Transform centroids back to original scale for plotting
    centroids = scaler.inverse_transform(centroids_scaled)
    
    print(f"Running K-Means for k = {k}...")

    # Plot clusters
    sns.scatterplot(data=df, x='Temperature', y='Absolute_magnitude', hue=f'Cluster_{k}', palette='viridis', ax=axes[i], s=60)
    
    # Mark Centroids
    axes[i].scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids', edgecolors='black')
    
    # HR Diagram conventions: Invert Temperature (X) & Magnitude (Y)
    axes[i].invert_xaxis()
    axes[i].invert_yaxis()
    
    axes[i].set_title(f'K-Means HR Diagram (k={k})')
    axes[i].set_xlabel('Temperature (K)')
    axes[i].set_ylabel('Absolute Magnitude (Mv)')
    axes[i].legend()

plt.tight_layout()
plt.savefig('HR_Diagram_Optimal.png')
plt.show()

print("\n################################################################################################################################\n\n")

# Evaluation: Confusion Matrix
for k in ks:
    print(f"\n💻 Confusion Matrix ( Actual Type vs Cluster Label for k={k} ) :\n")
    print(confusion_matrix(df['Star_type'], df[f'Cluster_{k}']))
    print('\n')

# Save the results
df.to_csv('Cluster Star Data.csv', index=False)
print("Results saved to 'Cluster Star Data.csv'")