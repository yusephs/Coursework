import matplotlib.pyplot as plt


labels = 'Certified Fresh', 'Fresh', 'Rotten'


data1 = [0.5, 0.2, 0.3]
data2 = [0.3, 0.4, 0.3]
fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.pie(data1, labels=labels, autopct='%.1f%%')
ax2.pie(data2, labels=labels, autopct='%.1f%%')

ax1.set_title("Matplotlib bakery: A pie")
ax2.set_title(" bakery: A pie")
plt.show()



