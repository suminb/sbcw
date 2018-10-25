# Lecture 1

세상은 [멱함수(power law)](https://en.wikipedia.org/wiki/Power_law)로 설명할 수 있는 것들이 많습니다. [파레토 법칙](https://en.wikipedia.org/wiki/Pareto_principle)이라고 설명하는 현상도 비슷한 맥락입니다. 20%의 인구가 80%의 부를 점유하고 있다거나, 80%의 매출이 20%의 고객으로부터 나온다는 이야기는 여러번 들어보셨을겁니다. 그뿐만이 아닙니다. 세상에는 수많은 과학자들이 존재하지만, 학계에 이름을 남기는 사람들은 소수에 불과합니다. 대중들에게 알려지는 사람은 그것보다 훨씬 극소수입니다. 사전에 존재하는 수많은 단어 중 우리가 일상 생활에서 사용하는 단어의 수는 제한적입니다. 특정 인구수를 가지는 도시들의 숫자는 인구수의 거듭제곱에 반비례하여 나타납니다. 

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Long_tail.svg/1000px-Long_tail.svg.png" style="max-width: 400px; display: block; margin: auto;">

이번 코딩 워크샵의 목표는 여러분에게 파이썬의 심오한 세계 중 20%를 소개함으로써 여러분이 꿈꾸는 일의 80%를 이룰 수 있도록 도와드리는 것입니다. 그런 의미에서 이 저장소에 올릴 강의 노트도 제가 실제 강의에서 이야기 할 내용의 20%만 올려놓도록 하겠습니다.

## 파이썬 코드 실행하기

파이썬 코드를 실행하는 방법에는 크게 두 가지가 있습니다. `python (파일 이름).py` 처럼 파이썬 코드 파일을 실행시키는 방법과 REPL에 코드를 한줄씩 실행하는 방법이 있습니다. 물론 [Flask의 디버거](http://werkzeug.pocoo.org/docs/0.14/debug/) 또는 [Jupyter Notebook](http://jupyter.org/)과 같은 다른 실행환경도 존재하지만, 표준 환경의 연장선이기 때문에 따로 구분하지는 않겠습니다.

### Python Read–Eval–Print Loop (REPL)

`python` 명령어에 파일 이름 등 별다른 인자를 주지 않고 실행하면 다음과 같이 REPL이 실행됩니다.

    Python 3.7.0 (default, Jun 29 2018, 20:13:13)
    [Clang 9.1.0 (clang-902.0.39.2)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

여기서 파이썬의 모든 기능을 사용할 수 있습니다. 아주 간단한 작업을 처리하거나, 익숙하지 않은 라이브러리르 사용할 때 한줄씩 실행 결과를 확인해 가면서 코드를 작성할 때에 유용합니다. 다음과 같이 계산기로 사용하거나,

    >>> 1000 * .425 / 365 * 14
    16.301369863013697

점심밥으로 무엇을 먹을 것인지 골라주는 코드를 작성해볼 수도 있습니다.

    >>> import random
    >>> random.choice(['페퍼로니 피자', '빅맥', '한방삼계탕', '똠양궁', '자루소바'])
    페퍼로니 피자

`_`는 바로 직전 결과 값을 나타냅니다.

    >>> 3 * 5
    15
    >>> _ - 4
    11

`dir()` 함수를 호출하여 특정 모듈이나 클래스에 어떤 멤버들이 있는지 알아볼 수 있습니다.

    >>> dir(random)
    ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_os', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

`type()` 함수도 유용하게 사용할 수 있습니다.

    >>> type(42)
    <class 'int'>
    >>> type(42.0)
    <class 'float'>
    >>> type('42')
    <class 'str'>

`help()` 함수는 파이썬 docstring의 내용을 보여줍니다.

    >>> help(random.randint)
    Help on method randint in module random:

    randint(a, b) method of random.Random instance
        Return random integer in range [a, b], including both end points.

종료하는 방법을 몰라서 당황할 수도 있는데, `exit()` 함수를 실행해서 종료하거나,

    >>> exit()

혹은, `ctrl + D` 키를 눌러서 [`EOF`](https://en.wikipedia.org/wiki/End-of-file)를 표준 입력으로 보냄으로써 인터프리터를 종료할 수도 있습니다.

### 파이썬 코드 파일 실행

매번 같은 코드를 REPL에 입력하는 것은 고통스러운 일이기 때문에 많은 경우 실행할 코드를 `.py` 파일에 저장해놓습니다. 예를 들어서, 파일 이름이 `test.py` 라고 가정할 때 다음과 같이 실행할 수 있습니다.

    python test.py

## 파이썬 코드 구성

### Entry point

C/C++, Java에는 `main()` 함수가 진입점이지만, 파이썬에는 그런 명시적인 진입점이 존재하지 않습니다. `python test.py` 와 같이 실행을 할 경우 `test.py`의 내용이 실행됩니다.

`test1.py`:
```python
import os

print(os.path.abspath(__file__))
```

실행을 하게 되면 다음과 같이 `test1.py` 스크립트의 절대경로가 출력됩니다.

```
$ python test1.py
/home/.../sbcw/fall2018/test1.py
```

NOTE: 참고로 REPL에서 같은 코드를 실행할 경우 `__file__`이 정의되지 않았기 때문에 오류가 발생합니다.

```
>>> os.path.abspath(__file__)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name '__file__' is not defined
```

파이썬 코드의 진입점은 코드를 어떻게 실행하는지에 따라 달라질 수 있습니다.

`test2.py`:
```python
import os

print(__name__)
```

다음과 같이 파이썬 인터프리터를 통해서 실행하게 되면 `__name__`의 값이 `__main__`이 됩니다.

```
$ python test2.py
__main__
```

하지만 다른 코드에서 `test2.py`를 임포트(import) 하게 되면 `__name__`은 해당 모듈의 이름이 됩니다.

```
>>> import test2
test2
```

이러한 차이점을 이용해서 다른 모듈에서 임포트 되었을 때에는 실행하지 않고, 파이썬 인터프리터를 통해서 실행했을 때에만 수행되는 코드를 작성할 수도 있습니다.

```python
if __name__ == '__main__':
    main()
```

### Modules

파이썬의 가장 큰 특징과 장점 중 하나는 풍부한 기본 라이브러리 이외에도 수많은 3rd-party 라이브러리가 있다는 점입니다. 어떤 일을 하고자 할 때 직접 만들기보다는 구글 검색 한번이면 필요한 기능을 찾을 수 있을 가능성이 매우 높습니다.

> There is ~~an app~~ a library for that.

```
parent/
    __init__.py
    one/
        __init__.py
    two/
        __init__.py
    three/
        __init__.py
```

Importing `parent.one` will implicitly execute `parent/__init__.py` and `parent/one/__init__.py`. Subsequent imports of `parent.two` or `parent.three` will execute `parent/two/__init__.py` and `parent/three/__init__.py` respectively.

- `import` statement
- `__import__()` function
- `importlib.import_module()`

Regular package: `module.py` or `module/__init__.py`

Refer [this](https://docs.python.org/3/reference/import.html) for more details.

### `import` statements

스타일 1:

```python
import os
```

스타일 2:

```python
from datetime import time
```

`import`문은 한 줄에 하나씩, 알파벳 순서대로 기술합니다.

Yes:
```python
import os
import sys
```

No:
```python
import sys, os
```

#### `import` orders

1. Standard library imports.
2. Related third party imports.
3. Local application/library specific imports.

```python
import os
import sys

from flask import Flask
import requests

from app import utils
```

#### `import` paths

1. Current module
2. `site-packages` of the current environment
3. Global environment

https://www.python.org/dev/peps/pep-0008/#imports

### White-space matters

파이썬에는 코드 블럭을 구분하는 장치가 공백 문자열입니다. `{}`를 사용하는 C/C++, Java 등의 언어와는 다른 점입니다. [PEP8](https://www.python.org/dev/peps/pep-0008/#indentation)에 따르면 코드 블럭을 구분하기 위해서 4개의 공백 문자열을 사용합니다.

```python
def withdraw(amount, balance):
    if amount > balance:
        # withdraw
    else:
        raise Exception('Insufficient balance')
```


## Primitive Types

파이썬에는 `int`, `long`, `float`, `bool`, `str` 등의 기본 타입이 있습니다. 이 부분에 대해서는 파이썬의 타입 시스템에 대해서 다룰 때 더 자세하게 설명할 예정입니다.

## Collections

- `list`
- `tuple`
- `set`
- `frozenset`
- `dict`

Q: `frozendict` 타입은 왜 없을까?

### List Indexing

    xs = [1, 2, 3, 4, 5, 6, 7]

Accessing indivdual elements:

    >>> xs[0]
    1
    >>> xs[1]
    2
    >>> xs[-1]
    7

Slicing:

    >>> xs[2:4]
    [3, 4]
    >>> xs[0:3]
    [1, 2, 3]
    >>> xs[0:-1]
    [1, 2, 3, 4, 5, 6]

Implicit slicing:

    >>> xs[3:]
    [4, 5, 6, 7]
    >>> xs[:2]
    [3, 4, 5, 6, 7]

Stepping:

    >>> xs[0:5:2]
    [1, 3, 5]

List concat:

    >>> [1, 2, 3] + [4, 5]
    [1, 2, 3, 4, 5]

Q: Explain how this works:

    >>> xs[::-1]
    [7, 6, 5, 4, 3, 2, 1]

Q: Why wouldn't it work for `set`s?

    >>> xs = set([1, 2, 3, 4, 5, 6, 7])
    >>> xs[0]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'set' object does not support indexing

## Control Statements

### `if` statement

```python
if expr1:
    # do something
    pass
elif expr2:
    # do something
    pass
else:
    # do something
    pass
```

```python
y = 'pass' if x else 'fail'
```

#### Explicit

```python
if x is not None:
    pass

if x != '':
    pass

if len(x) > 0:
    pass

if x != []:
    pass

if x != {}:
    pass
```

#### Implicit

```python
if x:
    pass
```

### `for` loop

```python
for var in iterable:
    # do something
    pass
```

    >>> for i in range(5):
    ...     print(i)
    ...
    0
    1
    2
    3
    4

`str`s are essentially `list`s:

    >>> for c in 'test':
    ...     print(c)
    ...
    t
    e
    s
    t

### `while` loop

```python
while expr:
    # do something
    pass
```

### Other Control Statements

- `try`/`except` statements
- `with` statement
- `switch` 는 없습니다. 하지만 만들 수는 있습니다. https://drive.google.com/file/d/1y9oBuTEdKYg3aphWO-R1u-15_1K2e29x/view

이건 다음 시간에 적절한 예제를 가지고 설명하도록 합시다.

## List Comprehension

    >>> xs = [1, 2, 3, 4, 5, 6, 7]
    >>> [x for x in xs]
    [1, 2, 3, 4, 5, 6, 7]

### Expressions

    >>> [x + 1 for x in xs]
    [2, 3, 4, 5, 6, 7, 8]

### Unpacking

    >>> xs = [1, 2, 3, 4]
    >>> ys = [1, 4, 9, 16]
    >>> [(x + y) for x, y in zip(xs, ys)]
    [2, 6, 12, 20]

zip? https://docs.python.org/3/library/functions.html#zip

### Nested list comprehension

    >>> [(x, y) for x in xs for y in ys]
    [(1, 1), (1, 4), (1, 9), (1, 16), (2, 1), (2, 4), (2, 9), (2, 16), (3, 1), (3, 4), (3, 9), (3, 16), (4, 1), (4, 4), (4, 9), (4, 16)]

https://www.python.org/dev/peps/pep-0202/

## Dict Comprehension

```python
items = ['apple', 'avocado', 'mango', 'orange']
quantities = [300, 1280, 600, 500]
```

    >>> inventory = {k: v for k, v in zip(items, quantities)}
    >>> inventory
    {'apple': 300, 'avocado': 1280, 'mango': 600, 'orange': 500}

    >>> inventory.items()
    dict_items([('apple', 300), ('avocado', 1280), ('mango', 600), ('orange', 500)])

## Generators

Generator functions allow you to declare a function that behaves like an iterator.

- Iterator 를 반환합니다.
- 느슨하게 평가(lazy evalution) 됩니다.
- Iterator 를 끝까지 소모하면 더이상 사용할 수 없습니다.

```python
def generator():
    yield 1
    yield 2
    yield 3
```

`next()` 함수를 호출하면 제네레이터가 생성한 원소를 하나씩 꺼내올 수 있습니다.

    g = generator()
    >>> next(g)
    1
    >>> next(g)
    2
    >>> next(g)
    3
    >>> next(g)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration

반복문이나 list comprehension 과 함께 사용할 수 있습니다.

    >>> for x in generator():
    ...     print(x)
    ...
    1
    2
    3

    >>> [x for x in generator()]
    [1, 2, 3]

    >>> list(generator())
    [1, 3, 3]

```python
def infinite_list():
    v = 0
    while True:
        yield v
        v += 1
```

느슨하게 평가 된다고 했으니 무한대 길이를 가지는 리스트를 만들어봅시다.

    >>> inf = infinite_list()

    >>> inf
    <generator object infinite_list at 0x10c2c55e8>

    >>> [next(inf) for _ in range(5)]
    [0, 1, 2, 3, 4]

Iterator 가 소진되면 더이상 사용할 수 없습니다.

    >>> g = generator()
    >>> [x for x in g]
    [1, 2, 3]
    >>> [x for x in g]
    []

Q. Why would you want to use generators?

## Functions

- Positional arguments
- Keyword arguments
- Arbitrary argument list
- Arbitrary keyword argument dictionary

## Taste of Real World

(판사님, 이 코드는 고양이가 만들었습니다.)

## 만약 시간이 허락한다면

- Coroutine: https://docs.python.org/3/library/asyncio-task.html
- Integer division vs. floating point division
- break, continue