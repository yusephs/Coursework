import csv
from pickle import TRUE
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('data2.csv', sep = '|')



print("\nPlease choose the first genre you would like to compare")
def Validation():
    global acf, af, ar, ag
    print("1- Comedy\n2- Drama\n3- Horror\n4- Classics\n5- Documentary\n6- Art House & International\n7- Action & Adventure\n")

    a = input("Please select a genre from 1-7\n")
    while a not in ["1", "2", "3", "4", "5", "6", "7"]:
        a = input("Please a valid input from 1-7\n")
        

    if (a == "1"):
        firstGenre = "Comedy"
    elif (a=="2"):
        firstGenre = "Drama"
    elif (a=="3"):
        firstGenre = "Horror"
    elif (a=="4"):
        firstGenre = "Classics"
    elif (a=="5"):
        firstGenre = "Documentary"
    elif (a=="6"):
        firstGenre = "Art House & International"
    elif (a=="7"):
        firstGenre = "Action & Adventure"


    acf =len(df[(df['genres']==firstGenre)&(df['tomatometer_status']=='Certified-Fresh')])
    af =len(df[(df['genres']==firstGenre)&(df['tomatometer_status']=='Fresh')])
    ar =len(df[(df['genres']==firstGenre)&(df['tomatometer_status']=='Rotten')])
    ag = acf+af+ar

Validation()
pacf = acf/ag
paf = af/ag
par = ar/ag


print("\nPlease choose the second genre you would like to compare")
Validation()

pbcf = acf/ag
pbf = af/ag
pbr = ar/ag


data1 = np.array([pacf, paf, par])
data2 = np.array([pbcf, pbf, pbr])

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.pie(data1)
ax2.pie(data2)

plt.show()