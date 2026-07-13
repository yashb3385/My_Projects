# Try to compare troops with similar use case
    # E.g. Comaring Healers with Dragon is useless

import csv
import pandas as pd

# Data Extraction
def cell(filename, row_index, col_index):
    """Prints a specific cell from a CSV file using pandas."""
    try:
        df = pd.read_csv(filename)
        return df.iloc[row_index, col_index]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Data Manupulation
from fpath import fp, fp2
dt = pd.read_csv(fp)
excluding_factors = ['DPH']

def pts(factor,pts):
    if cell(fp, j, i) == factor:
        l.append(pts)
    else:
        pass

Data = []
for j in range(dt.shape[0]):
    p = []
    l = [cell(fp, j, 0)]
    for i in range(1,dt.shape[1]):
        if cell(fp, j, 0) == 'Preferred Target':
            pts('Nothing', 0.5)
            pts('Defenses', 1)
        elif cell(fp, j, 0) == 'Targets':
            pts('Ground', 0.5)
            pts('Ground & Air', 1)      
        elif cell(fp, j, 0) == 'Attack Type':
            pts('Splash', 0.8)
            pts('Chain', 1)
            pts('Single', 0.5)
        elif cell(fp, j, 0) == 'Space' or cell('data.csv', j, 0) == 'Attack Speed(sec.)':
            p += [1/float(cell(fp, j, i))]
        elif cell(fp, j, 0) == 'Damage Decay(%)':
            p += [1-(float(cell(fp, j, i))/100)]
        elif cell(fp, j, 0) in excluding_factors:
            pass
        else:        
            p += [float(cell(fp, j, i))]
    
    if p == []:
        pass
    else:    
        for k in p:
            l.append(k/max(p))

    Data += [l]

Total_efficiency_list = ['Total Efficiency']
Damage_efficiency_list = ['Damage Efficiency']
Strategy_efficiency_list = ['Strategy Efficiency']
for k in range(1, dt.shape[1]):
    Damage_efficiency = 0
    Strategy_efficiency = 0
    for z in Data:
        if z[0] == 'Preferred Target' or z[0] == 'Attack Type':
            Strategy_efficiency += z[k]
        elif z[0] in excluding_factors:
            pass
        else:
            Damage_efficiency += z[k]
    Damage_efficiency_list += [Damage_efficiency]
    Strategy_efficiency_list += [Strategy_efficiency]
    Total_efficiency_list += [Damage_efficiency + Strategy_efficiency]     
   

with open(fp, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Reads the first row (header)
Data = [header] + Data + [[],[]] + [Damage_efficiency_list] + [Strategy_efficiency_list] + [Total_efficiency_list]

print('\n\n\nRelative Efficiency Data :\n')    
print(Data)
print('\n\nDamage Efficiency List :\n')
print(Damage_efficiency_list)
print('\n\nStrategy Efficiency List :\n')
print(Strategy_efficiency_list)
print('\n\nTotal Efficiency List :\n')
print(Total_efficiency_list) 

with open(fp2, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Data)
print(f"\n\nCSV file {fp2} updated successfully.\n\n\n")
