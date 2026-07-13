import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import csv

from fpath import fp2
def graph(troop_name):
    data = pd.read_csv(fp2)

    data_new = {'data type' : [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 1]}
    df_new = pd.DataFrame(data_new)
    data = pd.concat([data, df_new], axis=1)

    data.dropna(inplace=True)

    plt.figure(figsize=(10, 13))
    sns.scatterplot(
        y = 'Troop',
        x = troop_name,
        hue = 'data type',
        palette = 'viridis',
        data = data,
        s = 50,
        alpha = 0.9
    )

    plt.title(troop_name, fontsize = 15, fontweight = 'bold')
    plt.xlabel("Efficiency")
    plt.ylabel("Efficiency Factors")

    plt.grid(True, linestyle="--", alpha=0.5)

    # Ploting
    plt.show()


with open(fp2, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

for i in header:
    if i != 'Troop':
        graph(i)
