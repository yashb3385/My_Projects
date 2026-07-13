import csv
import pandas as pd
# Data Creation
data = [                                                              
    ['Troop','Dragon(lvl.8)','Electro(lvl.4)','Dragon Rider(lvl.2)','Balloon(lvl.9)'],  # Weightage
    ['DPS', 330, 330, 370, 256],                                                        #     1
    ['Hitpoints', 4200, 4500, 4400, 940],                                               #     1
    ['DPH', 412.5, 1155, 444, 768],   # must not be included                            #     1
    ['Damage When Destroyed', 0, 570, 800, 322],                                        #     1
    ['Death Damage Radius', 0, 4, 2, 1.2],                                              #     1
    ['Range', 3, 3, 4, 0.5],                                                            #     1
    ['Movement Speed', 16, 13, 20, 10],                                                 #     1
    ['Space', 20, 30, 25, 5],                                                           #     1
    ['Damage Decay(%)',0 ,20, 100, 0],                                                  #     1
    ['Total Targets', 1, 5, 1, 3],                                                      #     1
    ['Targets', 'Ground & Air', 'Ground & Air', 'Ground', 'Ground',],                   #    1.50                                  
    ['Preferred Target', 'Nothing', 'Nothing', 'Defenses', 'Defenses'],                 #    1.45  
    ['Attack Type',  'Splash' ,'Chain' ,'Single', 'Splash']                             #    1.80
]

from fpath import fp

with open(fp, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print(f"\n\nCSV file {fp} created successfully.")

# Shape of the csv file
df = pd.read_csv(fp)
print('\nShape of the data :',df.shape)
print(f'No. of Rows {df.shape[0]}')
print(f'No. of Columns {df.shape[1]}\n')

# Header of csv file
with open(fp, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Reads the first row (header)
print('Header :',header,'\n\n')



