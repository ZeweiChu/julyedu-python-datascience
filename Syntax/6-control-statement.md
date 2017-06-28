# control statement

回顾一下什么是boolean类型

```
>>> True
True
>>> False
False
```

然而有很多别的类型的value/variable也可以转化成boolean类型



```
import sys
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("""Usage: 
			python basic.py [your name]""")
		exit(-1)

	print("Hello {} from {}".format(sys.argv[1], sys.argv[0]))
```

我们尝试执行一下上一个小程序
```
$ python basic.py 
Usage: 
			python basic.py [your name]
$ python basic.py July
Hello July from basic.py
```
