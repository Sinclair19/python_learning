from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """一个生成随机漫步数据的类。"""
    def __init__(self, num_points=50000):
        """初始化随机漫步的属性。"""
        self.num_points = num_points
        #所有随机漫步都始于(0, 0)。
        self.x_values = [0]
        self.y_values = [0]
    def get_step(self):
        # 决定前进方向以及沿这个方向前进的距离。
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        if step == 0:
            self.get_step()
        return step
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x = self.x_values[-1] + self.get_step()
            y = self.y_values[-1] + self.get_step()
            self.x_values.append(x)
            self.y_values.append(y)
    
rw = RandomWalk()
rw.fill_walk()
plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
ax.scatter(0,0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.savefig('15-5.png',bbox_inches='tight')