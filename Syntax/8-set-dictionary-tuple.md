# more on list, set, dictionary, tuple

## more on list

### stack



### queue
```
>>> from collections import deque
>>> queue = deque(["julyedu", "fb", "google", "amazon"])
>>> queue.append("apple")
>>> queue
deque(['julyedu', 'fb', 'google', 'amazon', 'apple'])
>>> queue.popleft()
'julyedu'
>>> queue
deque(['fb', 'google', 'amazon', 'apple'])
>>> queue.pop()
'apple'
>>> queue
deque(['fb', 'google', 'amazon'])
```

更多关于deque的信息请查看[deque](https://docs.python.org/3/library/collections.html#collections.deque)

### 复习一下我们的list comprehension
```
>>> instructors = ["Han", "Chu", "July", "Wang"]
>>> ["Mr. " + i for i in instructors]
['Mr. Han', 'Mr. Chu', 'Mr. July', 'Mr. Wang']
```

如果我们想加上一些判断语句呢？
```
>>> ["Mr. " + i for i in instructors if i != "Wang"]
['Mr. Han', 'Mr. Chu', 'Mr. July']
>>> ["Mr. " + i if i != "Wang" else "Ms. " + i for i in instructors]
['Mr. Han', 'Mr. Chu', 'Mr. July', 'Ms. Wang']
```

## nested list comprehension



#### 小练习
```
>>> instructors = [["Han", "male"], ["July", "male"], ["Wang", "female"], ["Chu", "male"]] 
>>> ["Mr. " + i[0] if i[1] == "male" else "Ms. " + i[0] for i in instructors]
['Mr. Han', 'Mr. July', 'Ms. Wang', 'Mr. Chu']
```

## set
```
>>> names = {"tensorflow", "pytorch", "julyedu", "jupyter", "python", "numpy"}
>>> names
{'numpy', 'jupyter', 'python', 'julyedu', 'pytorch', 'tensorflow'}
>>> type(names)
<class 'set'>
```


```
>>> empty_set = set()
>>> empty_set
set()
```

- list可以被转换成set，可以用于去重
```
>>> numbers = [1,4,5,2,1,5,4,2]
>>> numbers
[1, 4, 5, 2, 1, 5, 4, 2]
>>> set(numbers)
{1, 2, 4, 5}
>>> list(set(numbers))
[1, 2, 4, 5]
```
- string也可以被转换成set
```
>>> set("banana")
{'b', 'n', 'a'}
```

- 比较fancy的一个例子, set comprehension
```
>>> {x for x in "banana" if x not in "an"}
{'b'}
```


## tuple


```
>>> t = 1, "facebook", "palo alto"
>>> t
(1, 'facebook', 'palo alto')
```

tuples有点像list，不过一个很大的区别是tuples是immutable的，也就是说它的element一旦创建之后就无法更改了。

```
>>> x, y, z = t
>>> x
1
>>> y
'facebook'
>>> z
'palo alto'
>>> t = list(t)
>>> t
[1, 'facebook', 'palo alto']
>>> x, y, z = t
>>> x
1
>>> y
'facebook'
>>> z
'palo alto'

```

## dictionary

dictionary就是字典，也就是把一个元素map到另一个元素上
```
>>> fruit
{'apple': 0, 'banana': 2, 'orange': 3, 'pineapple': 4}
>>> fruit["apple"]
0
>>> fruit["banana"]
2
```

下面的方法可以帮助我们查看一个dictionary的keys和values
```
>>> fruit.keys()
dict_keys(['apple', 'banana', 'orange', 'pineapple'])
>>> fruit.values()
dict_values([0, 2, 3, 4])

```

- 一个list of tuples也可以转换成dict。
```
>>> schools = dict([("Harvard",1), ("Princeton",2), ("Yale",3), ("Stanford",4), ("MIT",5), ("Chicago",6)])
>>> schools
{'Harvard': 1, 'Princeton': 2, 'Yale': 3, 'Stanford': 4, 'MIT': 5, 'Chicago': 6}
```

有时候我们想把一个list编号做成一个dictionary，比如下面这种情况:
```
>>> vocab = ["apple", "bit", "chrome", "face", "google", "hack", "intern", "jack", "kaggle"]
>>> vocab
['apple', 'bit', 'chrome', 'face', 'google', 'hack', 'intern', 'jack', 'kaggle']
>>> vocab2idx = {v:k for k, v in enumerate(vocab)}
>>> vocab2idx
{'apple': 0, 'bit': 1, 'chrome': 2, 'face': 3, 'google': 4, 'hack': 5, 'intern': 6, 'jack': 7, 'kaggle': 8}
```



