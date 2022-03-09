import csv
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('data2.csv', sep = '|')


a = input("What is the first genre you would like to compare\n").title()
print("")
b = input("What is the second genre you would like to compare\n").title()


acf =len(df[(df['genres']==a)&(df['tomatometer_status']=='Certified-Fresh')])
af =len(df[(df['genres']==a)&(df['tomatometer_status']=='Fresh')])
ar =len(df[(df['genres']==a)&(df['tomatometer_status']=='Rotten')])
ag =len(df[(df['genres']==a)])

bcf =len(df[(df['genres']==b)&(df['tomatometer_status']=='Certified-Fresh')])
bf =len(df[(df['genres']==b)&(df['tomatometer_status']=='Fresh')])
br =len(df[(df['genres']==b)&(df['tomatometer_status']=='Rotten')])
bg =len(df[(df['genres']==b)])


pacf = 100*acf/ag
paf = 100*af/ag
par = 100*ar/ag

pbcf = 100*bcf/bg
pbf = 100*bf/bg
pbr = 100*br/bg


print("percentage of certified fresh is: " + "%.2f" % pacf)
print("percentage of fresh is: " + "%.2f" % paf)
print("percentage of rotten is: " + "%.2f" % par + "\n")

print("percentage of certified fresh is: " + "%.2f" % pbcf)
print("percentage of fresh is: " + "%.2f" % pbf)
print("percentage of rotten is: " + "%.2f" % pbr)
plt.plot(df.movie_title, df.audience_rating)
plt.show()
