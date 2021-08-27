# 12武装飞船

### 12.3.1创建Pygame窗口及响应用户输入
alien_invasion.py
`pygame.display.flip()` 命令Pygame让最近绘制的屏幕可见

## 12.4添加飞船图像
Pygame默认加载位图。虽然可配置Pygame以使用其他文件类型，但有些文件类型要求你在计算机上安装相应的图像库

### 12.4.1创建Ship 类
ship.py

处理`rect`对象时，可使用矩形四角和中心的`x`坐标和`y`坐标。
可通过设置这些值来指定矩形的位置。要让游戏元素居中，可设置相应rect对象的属性`center` 、`centerx` 或`centery`
要让游戏元素与屏幕边缘对齐，可使用属性`top` 、`bottom` 、`left` 或`right`
除此之外，还有一些组合属性，如`midbottom` 、`midtop` 、`midleft` 和`midright`
要调整游戏元素的水平或垂直位置，可使用属性`x` 和`y`，分别是相应矩形左上角的`x`坐标和`y`坐标

### 12.4.2在屏幕上绘制飞船

## 12.5重构：方法`_check_events()` 和`__update_screen()`
**辅助方法** 在类中执行任务，但并非是通过实例调用的。在Python中，辅助方法的名称以单个下划线打头。

### 12.5.1方法`_check_events()`

## 12.6驾驶飞船

### 12.6.1响应按键

### 12.6.2允许持续移动