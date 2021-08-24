# 15生成数据

## 15.2绘制简单的折线图
mpl_squares.py
`import matplotlib.pyplot as plt`导入matplotlib.pyplot
变量`fig`表示整张图片。变量`ax`表示图片中的各个图表

方法`plot()`，它尝试根据给定的数据以有意义的方式绘制图表
函数`plt.show()`打开Matplotlib查看器并显示绘制的图表

## 15.2.1修改标签文字和线条粗细
参数`linewidth`决定了`plot()` 绘制的线条粗细。
参数`fontsize`指定图表中各种文字的大小
方法`set_xlabel()` 和`set_ylabel()` 让你能够为每条轴设置标题

方法`tick_params()`设置刻度的样式
其中指定的实参将影响 轴和 轴上的刻度（`axes='both'` ），并将刻度标记的字号设置为14（`labelsize=14` ）

### 15.2.2校正图形
向`plot()`提供一系列数时，它假设第一个数据点对应的x坐标值为0，

### 15.2.3使用内置样式
`plt.style.use()`使用内置主题

### 15.2.4使用`scatter()`绘制散点图并设置样式
向它传递一对x坐标和y坐标，它将在指定位置绘制一个点

### 15.2.6自动计算数据
`ax.axis([0, 1100, 0, 1100000])`
x坐标最小，最大，y坐标最小，最大范围

### 15.2.7自定义颜色
`ax.scatter(x_values, y_values, c='red', s=10)`
`ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)`

### 15.2.8使用颜色映射
`ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)`

### 15.2.9自动保存图表
`plt.savefig('squares_plot.png', bbox_inches='tight')`
第一个实参指定要以什么文件名保存图表，这个文件将存储到scatter_squares.py所在的目录。
第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白区域，只需省略这个实参即可。

## 15.3随机漫步

### 15.3.1创建`RandomWalk`类
randomwalk.py
```py
from random import choice
class RandomWalk:
    """一个生成随机漫步数据的类。"""
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性。"""
        self.num_points = num_points
        #所有随机漫步都始于(0, 0)。
        self.x_values = [0]
        self.y_values = [0]
```
### 15.3.2选择方向

### 15.3.5设置随机漫步图的样式
1. 给点着色
   我们将使用颜色映射来指出漫步中各点的先后顺序，并删除每个点的黑色轮廓，让其颜色更为明显。
2. 重新绘制起点和终点
3. 隐藏坐标轴
   `ax.get_xaxis().set_visible(False)`
4. 增加点数
5. 调整尺寸以适合屏幕
   `fig, ax = plt.subplots(figsize=(10, 6), dpi=128)`

## 15.4使用Plotly模拟掷骰子

### 15.4.2创建`Die`类
`from random import randint`
`randint(a,b)`
返回a，b之间的任何整数，包括a，b

### 15.4.4分析结果

### 15.4.5绘制直方图

### 15.4.6同时掷两个骰子
die.py

### 15.4.7同时掷两个面数不同的骰子

# 16下载数据

## 16.1`CSV`文件格式
要在文本文件中存储数据，一个简单方式是将数据作为一系列以逗号分隔的值写入文件。这样的文件称为`CSV`文件

### 16.1.1分析`CSV`文件头
`import csv`
`reader`处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中

### 16.1.2打印文件头及其位置
```py
for index, column_header in enumerate(header_row):
   print(index, column_header)
```

### 16.1.3提取并读取数据

### 16.1.4绘制温度图表

### 16.1.5模块datetime
|实参 |含义|
|:---|:---|
|%A |星期几，如Monday|
|%B |月份名，如January|
|%m |用数表示的月份（01～12）|
|%d |用数表示的月份中的一天（01～31）|
|%Y |四位的年份，如2019|
|%y |两位的年份，如19|
|%H |24小时制的小时数（00～23）|
|%I |12小时制的小时数（01～12）|
|%p |am或pm|
|%M |分钟数（00～59）|
|%S |秒数（00～61）|

### 16.1.6在图表中添加日期
`datetime.strptime=(row[], '%Y-%m-%d')`
`fig.autofmt_xdate()`绘制倾斜的日期标签

### 16.1.7涵盖更长的时间

### 16.1.8再绘制一个数据系列

### 16.1.9给图表区域着色
使用方法`fill_between()`。它接受一个x值系列和两个y值系列，并填充两个y值系列之间的空间
`ax.plot(dates, highs, c='red', alpha=0.5)`

### 16.1.10错误检查

### 16.1.11自己动手下载数据

## 16.2制作全球地震散点图：JSON格式

### 16.2.1地震数据
```py
import json
# 探索数据的结构。
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
   all_eq_data = json.load(f)
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
   json.dump(all_eq_data, f, indent=4)
```
函数`json.load()`将数据转换为Python能够处理的格式，这里是一个庞大的字典
`json.dump()`接受一个JSON数据对象和一个文件对象，并将数据写入这个文件
参数`indent=4`让`dump()`使用与数据结构匹配的缩进量来设置数据的格式

### 16.2.3创建地震列表

### 16.2.4提取震级

### 16.2.5提取位置数据

### 16.2.6绘制震级散点图

### 16.2.7另一种指定图表数据的方式
```py
import pandas as pd
data = pd.DataFrame(
data=zip(lons, lats, titles, mags), columns=["经度", "纬度", "位置", "震级"])
data.head()
```

### 16.2.8定制标记的尺寸
```py
fig = px.scatter(
   data,
   x="经度",
   y="纬度",
   range_x=[-200, 200],
   range_y=[-90, 90],
   width=800,
   height=800,
   title="全球地震散点图",
   size="震级",
   size_max=10,
)
fig.write_html("global_earthquakes.html")
fig.show()
```
标记尺寸默认为20像素，还可以通过`size_max=10`将最大显示尺寸缩放到10

### 16.2.9定制标记的颜色
默认的视觉映射图例渐变色范围是从蓝到红再到黄，数值越小则标记越蓝，而数值越大则标记越黄

### 16.2.10其他渐变
Plotly Express将渐变存储在模块`colors`中。这些渐变是在列表`px.colors.named_colorscales()`

Plotly除了有`px.colors.diverging` 表示连续变量的配色方案，
还有`px.colors.sequential` 和`px.colors.qualitative` 表示离散变量。

### 16.2.11添加鼠标指向时显示的文本
`hover_name="位置",`

***

# 17使用API

## 17.1使用Web API

### 17.1.1Git和GitHub

### 17.1.2使用API调用请求数据

### 17.1.4处理API响应
```py
import requests
# 执行API调用并存储响应。
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# 将API响应赋给一个变量。
response_dict = r.json()
# 处理结果。
print(response_dict.keys())
```

### 17.1.5处理响应字典

### 17.1.6概述最受欢迎的仓库

### 17.1.7监视API的速率限制

## 17.2使用Plotly可视化仓库
python_repos_visual.py

### 17.2.3在图表中添加可单击的链接
可使用html语法

### 17.2.4深入了解Plotly和GitHub API

## 17.3Hacker News API
hn_submissions.py