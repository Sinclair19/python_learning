from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint

class Die:
    """表示一个骰子的类。"""
    def __init__(self, num_sides=8):
        """骰子默认为6面。"""
        self.num_sides = num_sides
    def roll(self):
        """"返回一个位于1和骰子面数之间的随机值。"""
        return randint(1, self.num_sides)

# 创建两个D6。
die_1 = Die()
die_2 = Die()
# 掷几次骰子并将结果存储在一个列表中。
results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# 分析结果。
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# 可视化结果。
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷两个D6 1000次的结果',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout},filename='d8_d8.html')