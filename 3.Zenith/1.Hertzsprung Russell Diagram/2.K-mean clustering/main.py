print("---------------------------------------------------------------------------------------------------------------------------------\n\n")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

# Load the dataset & rename columns for accessibility
df = pd.read_csv('Dataset.csv')
df.columns = ['Temperature', 'Luminosity', 'Radius', 'Absolute_magnitude', 'Star_type', 'Star_color', 'Spectral_class']

# Convert to numeric values(i.e.'float' or 'int')
df = df.apply(pd.to_numeric, errors="coerce")

print("################################################################################################################################\n\n")
# Dropping rows with missing values(i.e. skipping them)
df.dropna(subset=['Temperature', 'Absolute_magnitude'], inplace=True)
print("                                        df\n\n\n", df, '\n')

print("################################################################################################################################\n\n")
# Select features for HR diagram (Temperature & Absolute Magnitude)
features = df[['Temperature', 'Absolute_magnitude']]
print("                                        features\n\n\n", features, '\n')

print("################################################################################################################################\n\n")
# Scale the features (K-Means is sensitive to the scale of data)
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features) # <class 'numpy.ndarray'>
print("                                        features_scaled\n\n\n", features_scaled, '\n')

print("################################################################################################################################\n\n")
# Perform K-Means Clustering & Visualization for different values of k
ks = [3, 4, 5, 6]      # Testing k=3 (Main Sequence, Giant, White Dwarf) & others
fig, axes = plt.subplots(1, len(ks), figsize=(20, 6))
print("                                        axes\n\n\n", axes, "\n")

for i, k in enumerate(ks):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(features_scaled)   # <class 'numpy.ndarray'>
    df[f'Cluster_{k}'] = clusters
    centroids_scaled = kmeans.cluster_centers_

    # Transform centroids back to original scale for plotting
    centroids = scaler.inverse_transform(centroids_scaled)
    
    # Print
    print(f"################################################################################################################################\n\n                                        For k = {k}\n\n\n")
    print(f"     kmeans\n\n", kmeans, "\n\n")
    print(f"     clusters\n\n", clusters, "\n\n")
    print(f"     centroids_scaled\n\n", centroids_scaled, "\n\n")
    print(f"     centroids\n\n", centroids ,"\n\n")

    # Plot clusters
    sns.scatterplot(data=df, x='Temperature', y='Absolute_magnitude', hue=f'Cluster_{k}', palette='viridis', ax=axes[i], s=60)
    
    # Mark Centroids
    axes[i].scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids', edgecolors='black')
    
    # HR Diagram conventions: Invert Temperature (X) & Magnitude (Y)
    axes[i].invert_xaxis()   # Values go from high to low
    axes[i].invert_yaxis()
    
    axes[i].set_title(f'K-Means HR Diagram (k={k})')
    axes[i].set_xlabel('Temperature (K)')
    axes[i].set_ylabel('Absolute Magnitude (Mv)')
    axes[i].legend()

print("################################################################################################################################\n\n")
print("                                        The updated 'df' is :\n\n\n", df)

plt.tight_layout()
plt.savefig('HR Diagram Clusters.png')   # Saves the plot
plt.show()

print("################################################################################################################################\n\n")
# Evaluation: Confusion Matrix (comparing clusters to actual labels)
for k in ks:
    print(f"\n💻 Confusion Matrix ( Actual Type vs Cluster Label for k={k} ) :\n")
    print(confusion_matrix(df['Star_type'], df[f'Cluster_{k}']))
    print('\n')

# Save the results to CSV
df.to_csv('Cluster Star Data.csv', index=False)