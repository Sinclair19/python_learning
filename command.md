
***

## 2.3字符串

### 2.3.1使用方法修改字符串的大小写
```python
txt = "test"
print()
print(txt.title()) #首字母大写
print(txt.upper()) #全部大写
print(txt.lower()) #全部小写
```
### 2.3.2在字符串中使用变量
```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
```
**python verison under 3.6**
```
full_name = "{} {}".format(first_name, last_name)
```

### 2.3.2使用制表符或换行符来添加空白
制表符`\t`
换行符`\n`

### 2.3.4删除空白
删除字符串末尾多余空白
`.rstrip()`
删除字符串开头多余空白
`.lstrip()`
删除字符串开头和末尾多余空白
`.strip()`

## 2.4数

### 2.4.1整数
`+ - * /`
乘方`**`

### 2.4.2浮点数

### 2.4.3整数和浮点数
将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除
如果一个操作数是整数，另一个操作数是浮点数，结果也总是浮点数

### 2.4.4数中的下划线
2.4.5同时给多个变量赋值
```python
x,y,z = 0,0,0
```

## 2.5注释

## Python之禅
```python
import this
```

***

# 3列表简介

## 3.1列表是什么

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```
输出结果
`['trek', 'cannondale', 'redline', 'specialized']`

### 3.1.1访问列表元素
`print(bicycles[0])`

### 3.1.2索引从0而不是1开始
将索引指定为-1 ，可让Python返回最后一个列表元素(-2,-3)

### 3.1.3使用列表中的各个值

## 3.2修改、添加和删除元素

### 3.2.1修改列表元素
`list[count] = `

### 3.2.2在列表中添加元素
1. 在列表末尾添加元素
   `append`
2. 在列表中插入元素
   `insert(destination,'item')`

### 3.2.3从列表中删除元素
1. 使用`del`语句删除元素
   `del list[destination]`
2. 使用方法`pop()`删除元素
   `list.pop()`
3. 弹出列表中任何位置处的元素
   `list.pop(destination)`
4. 根据值删除元素
   `list.remove('item')`

## 3.3组织列表

### 3.3.1使用方法`sort()`对列表永久排序
1. `sort()`按字母顺序排列
   无法恢复到原来的排列顺序
2. `sort(reverse=True)`按与字母顺序相反的顺序排列列表元素

### 3.3.2使用函数`sorted()`对列表临时排序
按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序

### 3.3.3倒着打印列表
`list.reverse()`反转列表元素顺序

### 3.3.4确定列表的长度
`len(list)`

## 3.4使用列表时避免索引错误