import csv
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('data2.csv', sep = '|')


a = input("What is the first genre you would like to compare\n").title()
print("")
b = input("What is the second genre you would like to compare\n").title()
 


bcf =len(df[(df['genres']==b)&(df['tomatometer_status']=='Certified-Fresh')])
nb =len(df[(df['genres']==a)&(df['tomatometer_status']!='Certified-Fresh' !='Fresh'!='Rotten')])
bf =len(df[(df['genres']==b)&(df['tomatometer_status']=='Fresh')])
br =len(df[(df['genres']==b)&(df['tomatometer_status']=='Rotten')])
bg =len(df[(df['genres']==b)]) - nb

pbcf = bcf/bg
pbf = bf/bg
pbr = br/bg

data1 = np.array([pacf, paf, par])
data2 = np.array([pbcf, pbf, pbr])

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.pie(data1)
ax2.pie(data2)

plt.show()