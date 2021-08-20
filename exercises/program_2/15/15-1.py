import matplotlib.pyplot as plt

x_values = range(1,5000)
y_values = [x**3 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.axis([0, 5000, 0, 25000000])
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s = 10)
plt.savefig('15-1.png',bbox_inches='tight')