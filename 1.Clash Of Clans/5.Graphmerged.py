import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import seaborn as sns
import csv

from fpath import fp2
data = pd.read_csv(fp2)


data_new = {'data type' : [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 1]}
df_new = pd.DataFrame(data_new)
data2 = pd.concat([data, df_new], axis=1)

def sctrplt(troop_name):
    sns.scatterplot(
            y = 'Troop',
            x = troop_name,
            hue = 'data type',
            palette = 'viridis',
            data = data2,
            s = 50,
            alpha = 0.9
        )

with open(fp2, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

style.use('ggplot')
for i in header:
    if i != 'Troop':
        plt.plot(data[i], data['Troop'], label = i , linewidth = 2)
        sctrplt(i)
plt.legend() 

plt.show()