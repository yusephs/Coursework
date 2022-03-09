import csv
import pandas as pd

df = pd.read_csv('data2.csv', sep = '|')

a = input("What is the first genre you would like to compare")
g1cf =len(df[(df['genres']==a)&(df['tomatometer_status']=='Certified-Fresh')])
g1f =len(df[(df['genres']==a)&(df['tomatometer_status']=='Fresh')])
g1r =len(df[(df['genres']==a)&(df['tomatometer_status']=='Rotten')])
g1 =len(df[(df['genres']==a)])
print("percentage of certified fresh is: " + 100*g1cf/g1)
print("percentage of fresh is: " + 100*g1f/g1)
print("percentage of rotten is: " + 100*g1r/12)

b = input("What is the second genre you would like to compare")
g2cf =len(df[(df['genres']==b)&(df['tomatometer_status']=='Certified-Fresh')])
g2f =len(df[(df['genres']==b)&(df['tomatometer_status']=='Fresh')])
g2r =len(df[(df['genres']==b)&(df['tomatometer_status']=='Rotten')])
g2 =len(df[(df['genres']==b)])
print("percentage of certified fresh is: " + 100*g2cf/g2)
print("percentage of fresh is: " + 100*g2f/g2)
print("percentage of rotten is: " + 100*g2r/g2)