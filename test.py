#import matplotlib.pyplot as plt
#import numpy as np

#y = np.array([35, 25, 25, 15])
#mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

#plt.pie(y, labels = mylabels, startangle = 90)
#plt.show() 

from matplotlib import pyplot as plt
import numpy as np

data1 = np.array([0.9, 0.1])
data2 = np.array([0.6, 0.4])

# create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2)

# plot each pie chart in a separate subplot
ax1.pie(data1)
ax2.pie(data2)

plt.show()