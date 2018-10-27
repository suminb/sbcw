# Lecture 4

참고: 이 강의 노트의 상당 부분은 https://realpython.com/primer-on-python-decorators/ 페이지를 참고하여 만들었다.

## Functions

- Functions vs. procedures
- Pure functions vs. non-pure functions
- Referential transparency

### Functions Are First-Class Objects

```python
def square(x):
    return x * x

def cube(x):
    return x ** 3
```

```
>>> square
<function square at 0x10ce431e0>

>>> square.__name__
'square'
```

```python
if exp == 2:
    func = square
elif exp == 3:
    func = cube

func(x)
```

```python
def power(base, exp):
    if exp == 2:
        return square
    elif exp == 3:
        return cube
    else:
        raise NotImplemented
```

### Inner Functions

(첫 시간에 간단하게 소개하고 넘어갔듯이) 파이썬에서는 함수 안에 함수를 정의하는 것이 가능하다.

```python
def parent():
    print('Printing from the parent() function')

    def first_child():
        print('Printing from the first_child() function')

    def second_child():
        print('Printing from the second_child() function')

    second_child()
    first_child()
```

내부 함수가 정의된 순서와는 관계 없이 호출한 순서대로 결과가 나오는 것을 확인할 수 있다.

```
>>> parent()
Printing from the parent() function
Printing from the second_child() function
Printing from the first_child() function
```

글로벌 스코프에서 내부 함수의 이름만 가지고 접근하는건 불가능하다.

```
>>> first_child()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'first_child' is not defined
```

### Returning Functions From Functions

```python
def parent():
    print('Printing from the parent() function')

    def first_child():
        print('Printing from the first_child() function')

    return first_child
```

```
>>> first_child = parent()
Printing from the parent() function

>>> first_child()
Printing from the first_child() function
```

## Simple Decorators

```python
def decorator(func):
    def wrapper():
        print('Something is happening before the function is called.')
        func()
        print('Something is happening after the function is called.')
    return wrapper

def meow():
    print('Meow!')

meow = decorator(meow)
```

```
>>> meow()
Something is happening before the function is called.
Meow!
Something is happening after the function is called.
```

간단하게 얘기해서: 데코레이터는 함수를 감싸서 함수의 동작을 변경할 수 있는 장치이다.

### Syntactic Sugar

`meow = decorator(meow)` 와 같이 수동으로 래핑하는 것은 아름답지 못하다. 함수를 래핑하기 용이하도록 [pie syntax](https://www.python.org/dev/peps/pep-0318/#background) 라고 불리는 문법 요소를 제공한다.

```python
def decorator(func):
    def wrapper():
        print('Something is happening before the function is called.')
        func()
        print('Something is happening after the function is called.')
    return wrapper

@decorator
def meow():
    print('Meow!')
```

```
>>> meow()
Something is happening before the function is called.
Meow!
Something is happening after the function is called.
```

### Reusing Decorators

다음과 같은 데코레이터를 `utils.py` 에 정의해놓았다고 가정한다.

```python
def repeat(func):
    def wrapper():
        func()
        func()
    return wrapper
```

```python
from utils import repeat

@repeat
def meow():
    print('Meow!')
```

```
>>> meow()
Meow!
Meow!
```

### Decorating Functions With Arguments

우리가 지금까지 사용했던 `meow()` 함수는 인자를 하나도 받지 않았지만, 인자를 받는 함수에 데코레이터를 적용한다면 문제가 발생한다.

```python
@repeat
def meow(name):
    print(f"Meow! I'm {name}")
```

```
>>> meow('Tom')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: wrapper() takes 0 positional arguments but 1 was given
```

데코레이터에서 인자를 하나도 전달해주지 않았기 때문인데, 다음과 같이 수정해서 해결할 수 있다.

```python
def repeat(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper
```

```
>>> meow('Tom')
Meow! I'm Tom
Meow! I'm Tom
```

### Returning Values From Decorated Functions

우리가 지금까지 정의했던 `meow()` 함수는 아무 값도 반환하지 않는다. `print()` 함수로 문자열을 출력하는 대신 문자열을 반환하고 싶다면 어떻게 해야 할까.

```python
@repeat
def meow(name):
    return f"Meow! I'm {name}"
```

이렇게 할 경우 다음과 같이 `None` 값을 반환하는 함수가 만들어진다. (파이썬에서는 아무 값도 반환하지 않는 함수를 정의하면 기본값으로 `None`을 반환한다.)

```
>>> meow('Tom') is None
True
```

위에서 데코레이터에서 아무런 값도 반환하지 않도록 정의했기 때문이다. 다음과 같이 수정해서 해결할 수 있다.

```python
def repeat(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs), func(*args, **kwargs)
    return wrapper
```

```
>>> meow('Tom')
("Meow! I'm Tom", "Meow! I'm Tom")
```

### Introspection Issues

NOTE: Introspection is the ability of an object to know about its own attributes at runtime.

일반적으로 함수의 속성은 런타임에 명확하게 알 수 있다.

```
>>> print
<built-in function print>

>>> print.__name__
'print'

>>> help(print)
Help on built-in function print in module builtins:

print(...)
    <full help message>
```

하지만 데코레이터로 감싼 함수의 경우 다음과 같이 정체성 혼란을 야기할 수 있다.

```
>>> meow
<function repeat.<locals>.wrapper at 0x106ae7378>

>>> meow.__name__
'wrapper'

>>> help(meow)
Help on function wrapper in module __main__:

wrapper(*args, **kwargs)
```

위와 같은 정체성 문제는 [`@functools.wraps`](https://docs.python.org/library/functools.html#functools.wraps) 데코레이터를 이용해서 해결할 수 있다.

```python
import functools

def repeat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs), func(*args, **kwargs)
    return wrapper
```

```
>>> meow
<function meow at 0x106aecc80>

>>> meow.__name__
'meow'

>> help(meow)
Help on function meow in module __main__:

meow(name)
```

### Taking Parameters

```python
@repeat(3)
def meow(name):
    return f"Meow! I'm {name}"
```

위와 같이 데코레이터에서 인자를 받고 싶으면 어떻게 해야 할까.

```python
import functools

def repeat(n=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(n)]
        return wrapper
    return decorator
```

```
>>> meow('Tom')
["Meow! I'm Tom", "Meow! I'm Tom", "Meow! I'm Tom"]
```


## Real World Examples

- <https://github.com/maxcountryman/flask-login/blob/3e521a326696cafbfbebfbb80a2fbffed68e6cf3/flask_login/utils.py#L221>
- <https://github.com/sh4nks/flask-caching/blob/34a84f705d5b7dd793257b6790be388b7bfcc994/flask_caching/__init__.py#L270>

## General Template

```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper
```