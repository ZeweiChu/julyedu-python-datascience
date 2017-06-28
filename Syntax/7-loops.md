# Loops

## 安装jupyter notebook
jupyter是一个非常方便的写python代码的工具
使用pip安装jupyter
```
pip install jupyter
````

使用下面的命令开启一个jupyter服务
```
jupyter notebook
```


## for loop

```
>>> names = ["Tensorflow", "July", "Keras", "Torch", "Caffe"]
>>> for name in names:
...  print(name)
... 
Tensorflow
July
Keras
Torch
Caffe 
```
不要忘了for语句后面包含的每一行都要缩进。

- range function
```
>>> for i in range(10):
...   print(i)
... 
0
1
2
3
4
5
6
7
8
9
```

关于range的用法
```
>>> list(range(1,10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(5,10))
[5, 6, 7, 8, 9]
>>> list(range(5,20,5))
[5, 10, 15]
>>> list(range(5,20,3))
[5, 8, 11, 14, 17]
>>> list(range(5,20,-1))
[]
>>> list(range(20,5,-1))
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
>>> list(range(20,5,-4))
[20, 16, 12, 8]
>>> list(range(20,5,-4))
```

如果我们想在每个element前面加个数字呢？
```
>>> for i in range(len(names)):
...   print(i, names[i])
... 
0 Tensorflow
1 July
2 Keras
3 Torch
4 Caffe
```

其实用enumerate更简
单，直接帮你带上数字
```
>>> for i, name in enumerate(names):
...  print(i, name)
... 
0 Tensorflow
1 July
2 Keras
3 Torch
4 Caffe
```

for与list在一起使用可以写很多简洁的语句, list comprehension
```
>>> ["stupid " + name for name in names]
['stupid Tensorflow', 'stupid July', 'stupid Keras', 'stupid Torch', 'stupid Caffe']
```
不要小瞧这个语句，将来你会发现很多地方用得到它。


## while loop

下面的这个小程序可以输出0-9
```
i = 0
while i < 10:
	print(i)
	i += 1
```
注意千万别忘了最后这一句```i += 1```否则就陷入死循环了。


### break和continue的用法
- break会直接让你跳出当前的循环
```
i = 0
while 1:
	print(i)
	i += 1
	if i >= 10:
		break
```

- continue则会让你结束当前循环的环节直接跳到下一循环
```
i = 0
while 1:
	if i % 5 == 0:
		i += 1
		continue
	print(i)
	i += 1
	
	if i >= 20:
		break
```


## 小练习：输出一个fibonacci数列
```
print("while loop:")
fibs = []
i = 0
j = 1
while i < 500:
	fibs.append(i)
	tmp = j
	j = i + j
	i = tmp
print(fibs)



print("for loop:")
fibs = [0, 1]
for i in range(2, 15):
	fibs.append(fibs[-1] + fibs[-2])

print(fibs)
```

