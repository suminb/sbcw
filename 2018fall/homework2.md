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
>>> d = DictWrapper({'a': 1, 'b': 2, 'c': 2})
>>> d.invert()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File ".../homework2_suminb.py", line 16, in invert
    raise ValueError('Dictionary is not injective, hence cannot be inverted')
ValueError: Dictionary is not injective, hence cannot be inverted
```

`invert()`가 반환하는 객체는 `dict` 타입이 아닌 `DictWrapper` 타입이어야 한다.

## Problem 2.1

파이썬의 `range()` 함수는 다음과 같이 유용하게 사용할 수 있다.

```
>>> [x for x in range(0, 10, 2)]
[0, 2, 4, 6, 8]
```

이것과 비슷한 기능을 제공하는 `Range` 클래스를 작성하여라. 단, `range()` 를 사용하지 않고 구현해야 한다. 또한, 복잡도를 줄이기 위해 `range(10)` 처럼 하나의 인자만 전달하는 것은 지원하지 않는다.

다음과 같이 시작과 끝을 명시하거나,

```
>>> [x for x in Range(0, 5)]
[0, 1, 2, 3, 4]
```

다음과 같이 시작과 끝, 그리고 스텝 크기를 명시할 수 있어야 한다.

```
>>> [x for x in Range(0, 10, 3)]
[0, 3, 6, 9]
```

세번째 인자인 `step`의 값은 `0`이 아닌 값이어야 하고, 만약 `0`이 주어진다면 `ValueError`를 내야 한다.

```
>>> Range(0, 0, 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File ".../homework2_suminb.py", line 23, in ...
    raise ValueError('`step` cannot be zero')
ValueError: `step` cannot be zero
```

다음의 파이썬 함수들이 도움이 될 수 있다.

- [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__)
- [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__)

## Problem 2.2

다음의 동작을 지원하도록 `Range` 클래스를 확장하여라.

```
>>> [x for x in reversed(Range(0, 5))]
[4, 3, 2, 1, 0]
```

```
>>> [x for x in reversed(Range(0, 10, 2))]
[8, 6, 4, 2, 0]
```

## 제출

답안은 `solutions/homework2_(GitHub 아이디).py` 파일로 제출하면 된다. 예를 들어서, GitHub 사용자 이름이 `suminb`라고 가정한다면 파일 이름은 `homework2_suminb.py`가 되어야 하고, 해당 파일을 `solutions` 디렉토리 안에 위치시키면 된다.

## 자동 채점

코드를 테스트 하기 위해서는 `pytest` 패키지가 필요하다. 다음의 명령어를 실행하여 설치하도록 한다.

    pip install pytest

패키지가 설치되면 다음과 같이 테스트 파일을 실행해서 여러분이 작성한 코드가 제대로 작동되는지 검증하도록 한다.

    pytest -v test_homework2.py --username (GitHub 아이디)