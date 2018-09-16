## Problem 1: JavaScript Dictionary

자바스크립트의 경우 `dict[key]` 또는 `dict.key` 를 구분하지 않고 사용할 수 있다. 반면, 파이썬에서는 이 둘의 용법이 명확하게 구분된다.

```
>>> d = DictWrapper({'key': 'value'})

>>> d['key']
value

>>> d.key
value
```

## Problem 1.1

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