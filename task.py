import csv
from pickle import TRUE
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('data2.csv', sep = '|')

while TRUE:
    a = input("What is the first genre you would like to compare\n").title()
    if (len(df.loc[df['genres']==a]) > 0 ):
        break

#    a = input("Enter a valid genre\n").title()


acf =len(df[(df['genres']==a)&(df['tomatometer_status']=='Certified-Fresh')]) 
#na =acf =len(df[(df['genres']==a)&(df['tomatometer_status'] !='Certified-Fresh' !='Fresh'!='Rotten')])
af =len(df[(df['genres']==a)&(df['tomatometer_status']=='Fresh')])
ar =len(df[(df['genres']==a)&(df['tomatometer_status']=='Rotten')])
ag = acf+af+ar
#ag =len(df[(df['genres']==a)]) Includes movies with missing tomatometer status

pacf = acf/ag
paf = af/ag
par = ar/ag

print("")
b = input("What is the second genre you would like to compare\n").title()
#if (df['genres']!=b):
#    b = input("Enter a valid genre\n").title()

bcf =len(df[(df['genres']==b)&(df['tomatometer_status']=='Certified-Fresh')])
#nb =len(df[(df['genres']==a)&(df['tomatometer_status']!='Certified-Fresh' !='Fresh'!='Rotten')])
bf =len(df[(df['genres']==b)&(df['tomatometer_status']=='Fresh')])
br =len(df[(df['genres']==b)&(df['tomatometer_status']=='Rotten')])
bg = bcf+bf+br
#bg =len(df[(df['genres']==b)]) Includes movies with missing tomatometer status


pbcf = bcf/bg
pbf = bf/bg
pbr = br/bg

#multiply the 6 variables above by 100
#print("Genre "+ a)
#print("percentage of certified fresh is: " + "%.2f" % pacf)
#print("percentage of fresh is: " + "%.2f" % paf)
#print("percentage of rotten is: " + "%.2f" % par + "\n")

#print("Genre "+ b)
#print("percentage of certified fresh is: " + "%.2f" % pbcf)
#print("percentage of fresh is: " + "%.2f" % pbf)
#print("percentage of rotten is: " + "%.2f" % pbr)

data1 = np.array([pacf, paf, par])
data2 = np.array([pbcf, pbf, pbr])

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.pie(data1)
ax2.pie(data2)

plt.show()