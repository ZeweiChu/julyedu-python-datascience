# Iterator and Generator

## iterator

- ```iter``` function
```
>>> x = iter([0, 1, 2, 3, 4, 5])
>>> next(x)
0
>>> next(x)
1
>>> next(x)
2
>>> next(x)
3
>>> next(x)
4
>>> next(x)
5
>>> next(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

定义一个class的时候，如果我们在class中定义```__iter__```和```__next__```两个method就能把这个class变成一个iterator。
```
class Yrange(object):
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration

for i in Yrange(12):
    print(i)

```





## Generator

```
ddef zrange(n):
    i = 0
    while i < n:
        yield(i)
        i += 1

for i in zrange(5):
    print(i)
```

## enumerate和zip

- enumerator
```
>>> names = ["FB", "GOOGLE", "APPLE", "AMAZON"]
>>> for i, name in enumerate(names):
...   print(i, name)
... 
0 FB
1 GOOGLE
2 APPLE
3 AMAZON
```

还有一个function叫做zip

```
>>> [ str(a) + str(b) for a, b in zip(names, numbers)]
['Tensorflow1', 'July2', 'Keras3', 'Torch4', 'Caffe5']

```
