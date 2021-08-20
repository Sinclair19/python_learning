import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.plot(x_values,y_values, linewidth=3)
ax.scatter(x_values,y_values, s=100)
# 设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
# 设置刻度标记的大小。
ax.tick_params(axis='both', labelsize=14)
plt.show()
