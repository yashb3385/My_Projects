# Importing Libraries
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
```

- **Pandas** $\to$ For handling `.csv` data & numerical arrays.
$\hspace{1cm}$
- **Matplotlib & Seaborn** $\to$ For creating the statistical graphs.
$\hspace{1cm}$
- **Scikit-Learn ( sklearn ) :**
	  1. `{python}KMeans` $\to$ The *Clustering* Algorithm.
	  2. `{python}StandardScaler` $\to$ *Normalizes* the data **(** *crucial for K-Means* **)**. Scales the data to be treated as equally.
	  3. `{python}confusion_matrix`: Used at the end to check *how accurate* the clustering was compared to the true labels.
--- 
# Data Preparation
```python
# Load the dataset & rename columns for accessibility
df = pd.read_csv('Dataset.csv')
df.columns = ['Temperature', 'Luminosity', 'Radius', 'Absolute_magnitude', 'Star_type', 'Star_color', 'Spectral_class']
```

- **Data Reading** $\to$ `{python}pd.read_csv('Dataset.csv')` reads the data  & stores its info. as `{python}df`.
$\hspace{1cm}$
- **Renaming** $\to$ The columns are renamed for *ease* of human reading using `{python}df.columns.`
--- 
# Convert to Numeric Values
```python
# Convert to numeric values(i.e.'float' or 'int')
df = df.apply(pd.to_numeric, errors="coerce")
```

- `{python}pd.to_numeric` $\to$ Try to convert all the values in the **columns** into numbers (*integers* or *floats*).
$\hspace{1cm}$
- `{python}errors="coerce"` $\to$ Replaces any invalid data with ‘ *NaN* ’ (missing values).
--- 
# Dropping the Missing Values
```python
# Dropping rows with missing values(i.e. skipping them)
df.dropna(subset=['Temperature', 'Absolute_magnitude'], inplace=True)
```

- It *Removes/Passes* the rows that have missing values so that the plot doesn’t break.
$\hspace{1cm}$
- `{python}inplace` :
  $\hspace{1cm}$
	  1. `{python}inplace=True` $\to$ It **modifies** the original DataFrame directly **(** *no copy* **)**.
	  2. `{python}inplace=False` **(** *Default* **)** $\to$ It returns a **new** DataFrame, leaving the *original unchanged*.
--- 
# Features Selection
```python
# Select features for HR diagram (Temperature & Absolute Magnitude)
features = df[['Temperature', 'Absolute_magnitude']]
```

- The **HR Diagram** is strictly a plot of *Temperature* **vs.** *Absolute Magnitude*. Therefore, only these two columns are selected as features.
--- 
# Scaling
```python
# Scale the features (K-Means is sensitive to the scale of data)
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features) # <class 'numpy.ndarray'>
```
## Working of `{python}StandardScaler`
It *squishes* both features into a similar range **(** *mean=0, variance=1* **)** so the algorithm treats them equally. It is because :

1. **Temperature** ranges from *2,000 to 40,000+ Kelvin*.
2. **Absolute Magnitude** ranges from *-10 to +20*.
## Working of `{python}fit_transform`
##### Step A: `{python}fit`
The scaler looks at your data and calculates two key statistics for every column:

1. **Mean ( $\mu$ ) :** The average value.
2. **Standard Deviation ( $\sigma$ ) :** How spread out the data is.
##### Step B: `{python}transform`
It applies the **Standardization** ( or *Z-score normalization* ) formula to every single data point:
$\hspace{1cm}$
$$z=\frac{x-\mu}{\sigma}$$
--- 
# Creating the Canvas `{python}plt.subplots`
```python
# Perform K-Means Clustering & Visualization for different values of k
ks = [3, 4, 5, 6]      # Testing k=3 (Main Sequence, Giant, White Dwarf) & others
fig, axes = plt.subplots(1, len(ks), figsize=(20, 6))
```

- `{python}ks` is list of all values of k **(** *k = No. of Clusters* **)**.
  $\hspace{1cm}$
- `{python}1, len(ks)` tells **Matplotlib** to create *1 row* and `{python}len(ks)` *columns* of plots.
  $\hspace{1cm}$
- `{python}figsize=(20, 6)` sets the appropriate size for the figure.
  $\hspace{1cm}$
- `{python}axes` is an **array** that holds each of these *three blank plots*, allowing us to draw on them one by one using a loop.
--- 
# The Clustering Loop
## Code of Whole Loop
```python
for i, k in enumerate(ks):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(features_scaled)   # <class 'numpy.ndarray'>
    df[f'Cluster_{k}'] = clusters
    centroids_scaled = kmeans.cluster_centers_

    # Transform centroids back to original scale for plotting
    centroids = scaler.inverse_transform(centroids_scaled)

    # Plot clusters
    sns.scatterplot(data=df, x='Temperature', y='Absolute_magnitude', hue=f'Cluster_{k}', palette='viridis', ax=axes[i], s=60)

    # Mark Centroids
    axes[i].scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids', edgecolors='black')

    # HR Diagram conventions: Invert Temperature (X) & Magnitude (Y)
    axes[i].invert_xaxis()   # Values go from high to low
    axes[i].invert_yaxis()
    axes[i].set_title(f'K-Means HR Diagram (k={k})')
    axes[i].set_xlabel('Temperature (K)')
    axes[i].set_ylabel('Absolute Magnitude (Mv)')
    axes[i].legend()
```
## The For Loop
`{python}enumerate(ks)` $\to$ This gives us both the index (`{python}i`) and the value (`{python}k`).

- When `{python}k=3`, `{python}i=0`.
- When `{python}k=4`, `{python}i=1`.
- When `{python}k=5`, `{python}i=2`.
- When `{python}k=6`, `{python}i=3`.
## Training the Data ( Running K-Means )
```python
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
clusters = kmeans.fit_predict(features_scaled)
```

- **`{python}n_clusters=k`** $\to$ Tells the computer how many *clusters* to form.
  $\hspace{1cm}$
- **`{python}random_state=42`** $\to$ K-Means starts by placing ' **centroids** ' (center points) randomly. Setting a *seed* (42) ensures that every time you run the code, the *random start is the same*, making your results reproducible.
  $\hspace{1cm}$
- **`{python}n_init=10`** $\to$ The **algorithm will run 10 times** with different random starting points and pick the best result to avoid getting stuck in a "bad" random start. It gives more *accuracy*.
  $\hspace{1cm}$
- `{python}kmeans.fit_predict()`:
  $\hspace{1cm}$
	  1. `{python}fit` $\to$ The algorithm starts the **K-Means** process.
	  2. `{python}predict` $\to$ The algorithm gives every star cluster a label **(** *0 to k−1* **)** for the finalized clusters.
## Handling Centroids
```python
df[f'Cluster_{k}'] = clusters
centroids_scaled = kmeans.cluster_centers_

# Transform centroids back to original scale for plotting
centroids = scaler.inverse_transform(centroids_scaled)
```

- `{python}df[f'Cluster_{k}'] = clusters` $\to$ K-Means has finished grouping the stars, but those labels (0, 1, 2...) are currently just sitting in a separate list in the computer's memory. This line takes those labels and sticks them back into your original table (`{python}df`) as a *new column* `{python}f'Cluster_{k}'`.
$\hspace{1cm}$
- `{python}cluster_centers_` $\to$ It returns an **array** of coordinates of *Centroids*.
  $\hspace{1cm}$
- `{python}inverse_transform` $\to$ It *scales* the coordinates *back* into real-world units.
  $\hspace{1cm}$
	  **The Math** $\to$ Earlier, we subtracted the mean and divided by the standard deviation. `{python}inverse_transform` does the opposite, it multiplies by the standard deviation and adds the mean back.
## Plotting the HR Diagram
```python
# Plot clusters
sns.scatterplot(data=df, x='Temperature', y='Absolute_magnitude', hue=f'Cluster_{k}', palette='viridis', ax=axes[i], s=60)

# Mark Centroids
axes[i].scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids', edgecolors='black')

# HR Diagram conventions: Invert Temperature (X) & Magnitude (Y)
axes[i].invert_xaxis()   # Values go from high to low
axes[i].invert_yaxis()
axes[i].set_title(f'K-Means HR Diagram (k={k})')
axes[i].set_xlabel('Temperature (K)')
axes[i].set_ylabel('Absolute Magnitude (Mv)')
axes[i].legend()
```

- `{python}centroid[:, x]` $\to$ This syntax follows the rule : `{python}array[rows, columns]`
  $\hspace{1cm}$
	  1. **The Colon (`:`)**: This means ' *Take All Rows*. '
	  2. **The Number (`0`** or **`1`)**: This specifies which column to grab.
$\hspace{1cm}$
		`{python}centroid[:, 0]` $\to$ This pulls out all the **Temperature** values for the *centers*.
		`{python}centroid[:, 1]` $\to$ This pulls out all the **Absolute Magnitude** values for the *centers*.
$\hspace{1cm}$
- `{python}axes[i]` $\to$ $i^{th}$ subplot.
$\hspace{1cm}$
- `{python}axes[i].legend()` $\to$ It adds a **key** or **label box** to your graph.
--- 
# Showing & Saving our Plot
```python
plt.tight_layout()
plt.savefig('HR Diagram Clusters.png')   # Saves the plot
plt.show()
```

- `{python}plt.tight_layout()` is a "cleanup" command. Its job is to automatically adjust the **padding** and **spacing between** your **subplots** so that everything fits neatly within the figure window.
--- 
# [[Confusing Matrix]]
```python
# Evaluation: Confusion Matrix (comparing clusters to actual labels)
for k in ks:
    print(f"\n💻 Confusion Matrix ( Actual Type vs Cluster Label for k={k} ) :\n")
    print(confusion_matrix(df['Star_type'], df[f'Cluster_{k}']))
```

- The dataset actually contains **k real star types**.
$\hspace{1cm}$
- The `{python}confusion_matrix` compares : **True Types** (*rows*) vs. the **K-Means Cluster Labels** (*columns*).
$\hspace{1cm}$
- **Goal** $\to$ A perfect clustering would result in a matrix where most numbers are on the *diagonal* (*or permuted diagonal*).
--- 
# Saving the results as csv file
```python
# Save the results to CSV
df.to_csv('Cluster Star Data.csv', index=False)
```
