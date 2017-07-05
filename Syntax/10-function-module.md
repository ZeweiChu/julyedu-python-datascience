# function, module

## function

- def关键词
- 用括号包含list of parameters
- statements都要indent


```
def fib(n):
	a, b = 0, 1
	for i in range(n):
		print(a, end=" ")
		a, b = b, a+b
	print()

fib(5)
fib(10)
fib(30)
fib(100)
```


### 不定长度的arguments
```
def print_all(*args):
	print(type(args))
	print(args)

print_all("hello", "world", "julyter", "notebook")
```

### default argument
concat例子


### 把一个tuple/list当做arguments

```
def unpack_args(a, b):
	print(a, b)

r = [2,5]
r = 2,5
unpack_args(r) # 会报错
unpack_args(*r) # 运行正常了
```

## modules

### 关于模块化(modularity)

function的作用是拿到一些参数，做一些运算或者别的更加复杂的操作，然后返回一些结果。


### 