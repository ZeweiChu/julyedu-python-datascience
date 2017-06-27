# List

list 是一种python的数据类型，表示一连串的数据的集合。


如何创建一个list
```
>>> names = ["Tensorflow", "July", "Keras", "Torch", "Caffe"]
>>> names
['Tensorflow', 'July', 'Keras', 'Torch', 'Caffe']
```

list indexing
```
>>> names[0]
'Tensorflow'
>>> names[1]
'July'
>>> names[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> names[4]
'Caffe'
>>> names[-1]
'Caffe'
>>> names[-5]
'Tensorflow'
>>> names[-10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

list slicing
```
>>> names[1:3]
['July', 'Keras']
>>> names[1:5]
['July', 'Keras', 'Torch', 'Caffe']
>>> names[1:7]
['July', 'Keras', 'Torch', 'Caffe']
>>> names[1:-1]
['July', 'Keras', 'Torch']
>>> names[1:0]
[]
```

我们可以直接把string变成一个list
```
>>> list("Julyedu")
['J', 'u', 'l', 'y', 'e', 'd', 'u']
```

求list的长度
```
>>> len(names)
5
```

append方法可以在list的末尾添加element
```
>>> names.append("Jack")
>>> names
['Tensorflow', 'July', 'Keras', 'Torch', 'Caffe', 'Jack']
>>> names.append(12)
>>> names.append(12.5)
>>> names.append([1,2,3])
>>> names
['Tensorflow', 'July', 'Keras', 'Torch', 'Caffe', 'Jack', 12, 12.5, [1, 2, 3]]
```
从上面这个例子我们也可以发现list可以嵌套list


两个list相加合并成新的list
>>> numbers = [1,2,3,4,5]
>>> names + numbers
['Tensorflow', 'July', 'Keras', 'Torch', 'Caffe', 'Jack', 12, 12.5, [1, 2, 3], 1, 2, 3, 4, 5]


