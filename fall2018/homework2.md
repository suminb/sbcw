## Problem 1: JavaScript Dictionary

자바스크립트의 경우 `dict[key]` 또는 `dict.key` 를 구분하지 않고 사용할 수 있다. 반면, 파이썬에서는 이 둘의 용법이 명확하게 구분된다.

```
>>> d = {'key': 'value'}

>>> d['key']
'value'

>>> d.key
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'key'
```


## Problem 1.1

```
>>> d = DictWrapper({'key': 'value'})

>>> d['key']
value

>>> d.key
value
```

위와 같이 이 둘을 명확하게 구분하지 않고 사용할 수 있도록 만들어주는 `DictWrapper` 클래스를 구현하여라.

```python
class DictWrapper(object):

    def __init__(self, dict_)
        pass

    def __getattr__(self, key):
        pass

    def __getitem__(self, key):
        pass
```

참고: 이것보다 훨씬 간단하게 구현할 수 있는 방법이 존재한다. 힌트는 '상속'.

## Problem 1.2

다음과 같이 값을 쓸 수 있도록 `DictWrapper`를 확장하여라.

```
>>> d = DictWrapper({'key': 'value'})

>>> d['key'] = 'new value'
>>> d['key']
new value

>>> d.key = 'another value'
>>> d['key']
another value
```

## Problem 1.3

키와 값의 관계가 1:1인지 (i.e., injective) 확인하는 메소드를 작성하여라.

```python
class DictWrapper(object):

    def injective(self):
        return False
```

예를 들어서, 1:1의 관계를 가지는 딕셔너리가 주어진다면 다음과 같은 결과가 나올 것이다.

```
>>> d = DictWrapper({'a': 1, 'b': 2, 'c': 3})
>>> d.injective()
True
```

반면, 1:1의 관계가 아니라면 다음과 같은 결과가 나와야 한다.

```
>>> d = DictWrapper({'a': 1, 'b': 2, 'c': 2})
>>> d.injective()
False
```

Injective functions 에 대한 더 자세한 내용은 [위키피디아 항목](https://en.wikipedia.org/wiki/Injective_function)을 참조하면 좋다.

## Problem 1.4

키와 값의 관계가 1:1일 때 (i.e., injective) 키와 값을 맞바꾸는 메소드를 작성하여라.

```python
class DictWrapper(object):

    def invert(self):
        pass
```

```
>>> d = DictWrapper({'a': 1, 'b': 2, 'c': 3})
>>> d.invert()
{1: 'a', 2: 'b', 3: 'c'}
```

만약 1:1 관계가 성립하지 않는다면 `ValueError`를 내야 한다.

```
>>> d = DictWrapper({'a': 1, 'b': 2, 'c': 3})
>>> d.invert()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File ".../solution2_suminb.py", line 16, in invert
    raise ValueError('Dictionary is not injective, hence cannot be inverted')
ValueError: Dictionary is not injective, hence cannot be inverted
```

`invert()`가 반환하는 객체는 `dict` 타입이 아닌 `DictWrapper` 타입이어야 한다.