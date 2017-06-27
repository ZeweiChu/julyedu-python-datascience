# 字符串(string)

## 基础
quote ' 和double quote " 都可以用作字符串
```
>>> "help"
'help'
>>> 'help'
'help'
```
两者之间在表示一个字符串上没有区别，但是一个字符串的开头和结尾必须使用同一种引号。
backslash \ 可以用来escape引号。
```
>>> 'I\'m gonna sleep early tonight'
"I'm gonna sleep early tonight"
```

当然也可以使用两种不同的引号来区分究竟是字符串结尾还是字符串中出现了引号。
```
>>> "I\'m gonna sleep early tonight"
"I'm gonna sleep early tonight"
```

如果一个string有好多行
```
>>> print("""first line
... second line
... third line""")
first line
second line
third line
```

\n 是换行符，可以用在strign中换行
```
>>> print("first line\nsecond line\nthirdline")
first line
second line
thirdline
```

\t是tab键
```
>>> print("first line\tsecond line\tthirdline")
first line	second line	thirdline
```

+可以把两个string连到一起
```
>>> "hello" + " " + "world"
'hello world'
```

## string indexing and slicing
- indexing
```
>>> w = "julyedu"
>>> w[0]
'j'
>>> w[1]
'u'
>>> w[-1]
'u'
>>> w[-3]
'e'
>>> w[-100]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> w[100]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

- slicing
```
IndexError: string index out of range
>>> w[1:3]
'ul'
>>> w[:3]
'jul'
>>> w[5:7]
'du'
>>> w[5:-1]
'd'
>>> w[5:]
'du'
>>> w[5:100]
'du'
>>> w[-1:10]
'u'
>>> w[-3:10]
'edu'
>>> w[-3:2]
''
```

## 字符串函数

- upper and lower
```
>>> w = "JulyEdu"
>>> w.upper()
'JULYEDU'
>>> w.lower()
'julyedu'
>>> w.capitalize()
'Julyedu'
```

- startswith and endswith
```
>>> w.endswith("du")
True
>>> w.endswith("u")
True
>>> w.startswith("J")
True
>>> w.startswith("j")
False
>>> w.startswith("Ju")
True
```

- strip
```
>>> w = "  Julyedu  "
>>> w.lstrip()
'Julyedu  '
>>> w.rstrip()
'  Julyedu'
>>> w.strip()
'Julyedu'
>>> 
```


- split
把一个string拆成一个list of strings
```
>>> s = "burger spaghetti fries steak dimsum ramen"
>>> s.split()
['burger', 'spaghetti', 'fries', 'steak', 'dimsum', 'ramen']
>>> s = "burger,spaghetti,fries,steak,dimsum,ramen"
>>> s.split(",")
['burger', 'spaghetti', 'fries', 'steak', 'dimsum', 'ramen']
```


- find: 找到第一个substring出现的位置
```
>>> w.find("ly")
2
>>> w.find("l")
2
```
如果输入一个不存在的substring那就会返回-1了
```
>>> w.find("a")
-1
```


- replace
>>> s.replace(",", ".")
'burger.spaghetti.fries.steak.dimsum.ramen'


更多信息在[官方document](https://docs.python.org/3.6/library/string.html)




