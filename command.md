##2.3字符串

###2.3.1使用方法修改字符串的大小写
```python
txt = "test"
print()
print(txt.title()) #首字母大写
print(txt.upper()) #全部大写
print(txt.lower()) #全部小写
```
###2.3.2在字符串中使用变量
```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
```
python verison under 3.6
```
full_name = "{} {}".format(first_name, last_name)

###2.3.2使用制表符或换行符来添加空白
制表符\t
换行符\n

###2.3.4删除空白
删除字符串末尾多余空白
.rstrip()
删除字符串开头多余空白
.lstrip()
删除字符串开头和末尾多余空白
.strip()

##2.4数

###2.4.1整数
+ - * /
乘方**
###2.4.2浮点数
###2.4.3整数和浮点数
将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除
如果一个操作数是整数，另一个操作数是浮点数，结果也总是浮点数
###2.4.4数中的下划线
2.4.5同时给多个变量赋值
```python
x,y,z = 0,0,0
```

##2.5注释

##Python之禅
```python
import this
```
