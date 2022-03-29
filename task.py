import csv
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('data2.csv', sep = '|')

def Validation():
    global acf, af, ar, ag, genre
    print("1- Comedy\n2- Drama\n3- Horror\n4- Classics\n5- Documentary\n6- Art House & International\n7- Action & Adventure\n")

    a = input("Please select a genre from 1-7\n")
    while a not in ["1", "2", "3", "4", "5", "6", "7"]:
        a = input("Please a valid input from 1-7\n")
        

    if (a == "1"):
        genre = "Comedy"
    elif (a=="2"):
        genre = "Drama"
    elif (a=="3"):
        genre = "Horror"
    elif (a=="4"):
        genre = "Classics"
    elif (a=="5"):
        genre = "Documentary"
    elif (a=="6"):
        genre = "Art House & International"
    elif (a=="7"):
        genre = "Action & Adventure"


    acf =len(df[(df['genres']==genre)&(df['tomatometer_status']=='Certified-Fresh')])
    af =len(df[(df['genres']==genre)&(df['tomatometer_status']=='Fresh')])
    ar =len(df[(df['genres']==genre)&(df['tomatometer_status']=='Rotten')])
    ag = acf+af+ar

print("\nPlease choose the first genre you would like to compare")
Validation()
pacf = acf/ag
paf = af/ag
par = ar/ag
firstGenre = genre

print("\nPlease choose the second genre you would like to compare")
Validation()
pbcf = acf/ag
pbf = af/ag
pbr = ar/ag
secondGenre = genre

data1 = [pacf, paf, par]
data2 = [pbcf, pbf, pbr]

labels = 'Certified Fresh', 'Fresh', 'Rotten'

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.pie(data1, labels=labels, autopct='%.1f%%')
ax2.pie(data2, labels=labels, autopct='%.1f%%')

ax1.set_title(firstGenre)
ax2.set_title(secondGenre)
plt.show()