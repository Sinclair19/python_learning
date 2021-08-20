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