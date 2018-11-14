# Homework 2

## Problem 1: Vector

벡터(`Vector`) 객체를 구현하는 것이 이 문제의 목표이다. 스켈레톤(skeleton) 구현은 다음과 같으며, 구현에 어려움이 있다면 이 섹션 맨 아래쪽에 있는 힌트를 참고해도 좋다. 힌트를 보기 전에 최대한 혼자 힘으로 해결해보는 것을 추천한다.

파일 이름은 `homework2.py` 로 한다.

```python
class Vector:

    def __init__(self, *elements):
        self.elements = elements

    def __eq__(self, other):
        return all([x == y for x, y in zip(self.elements, other.elements)])

    # ...
```

### Problem 1.1

벡터는 최소 두 개 이상의 원소로 이루어진 값이다. 다음과 같이 생성할 수 있다.

```
>>> Vector(1, 2, 3, 4)
<__main__.Vector object at 0x1063640b8>
```

두 개 미만의 원소로 벡터를 생성하려고 시도하면 다음과 같이 `ValueError`가 발생한다.

```
>>> Vector(1)
Traceback (most recent call last):
  File "...", line 7, in __init__
    raise ValueError('At least two elements are required')
ValueError: At least two elements are required
```

### Problem 1.2

```
>>> Vector(1, 2, 3, 4)
<__main__.Vector object at 0x1063640b8>
```

위와 같이 메모리 주소가 나오는 것 보다는

```
>>> Vector(1, 2, 3, 4)
[1, 2, 3, 4]
```

이처럼 쉽게 인지할 수 있는 형식으로 출력하는 것이 여러모로 도움이 된다. 이렇게 나올 수 있도록 built-in 메소드를 오버라이드 해보자.

### Problem 1.3

벡터 객체를 생성했다면 크기를 알 수 있어야 한다.

```
>>> v = Vector(3, 5, 7)
>>> len(v)
3
```

### Problem 1.4

기본적인 동작 중 하나인 negation 을 구현하여라.

```
>>> v = Vector(1, -2, 3)
>>> -v
[-1, 2, -3]
```

### Problem 1.5

벡터의 덧셈 연산을 구현하여라.

```
>>> u = Vector(5, 0, 4)
>>> v = Vector(1, -2, 3)
>>> u + v
[6, -2, 7]
```

만약 두 벡터의 길이가 같지 않다면 `ValueError` 를 내야 한다.

```
>>> Vector(1, 2, 3) + Vector(1, 2, 3, 4)
Traceback (most recent call last):
  File "...", line 45, in ...
    raise ValueError(f'A vector of size {len(self)} is expected')
ValueError: A vector of size 3 is expected
```

### Problem 1.6

벡터의 뺄셈 연산을 구현하여라.

```
>>> u = Vector(5, 0, 4)
>>> v = Vector(1, -2, 3)

>>> u - v
[4, 2, 1]

>>> v - u
[-4, -2, -1]
```

뺄셈 연산도 덧셈 연산과 마찬가지로 양쪽 항 벡터의 크기가 같아야 한다.

### Problem 1.7

벡터의 곱셈을 구현하여라. 두 가지 종류의 곱셈 연산을 지원한다.

```
>>> u = Vector(1, 3, -5)
>>> v = Vector(4, -2, -1)
```

위와 같이 벡터 `u`, `v`가 정의된다고 할 때, 다음과 같이 scalar 값과의 곱셈 연산을 지원해야 한다.

Bonus problem: `2 * u` 와 같은 형태의 연산을 지원하려면 어떻게 해야 할까?

```
>>> u * 2
[2, 6, -10]
```

벡터끼리 곱하는 것은 [dot product](https://en.wikipedia.org/wiki/Dot_product)로 정의된다.

```
>>> u * v
3
```

### Problem 1.8

벡터끼리의 나눗셈은 정의되지 않는다.

```
>>> u / v
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'Vector' and 'Vector'
```

정수형 나눗셈의 경우에도 마찬가지다.

```
>>> u // v
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for //: 'Vector' and 'Vector'
```

단, scalar 값으로 나누는 경우는 다룰 수 있어야 한다.

```
>>> u / 2
[1.0, 1.5, 2.0, 2.5]
```

정수형 나눗셈의 경우도 마찬가지다.

```
>>> u // 2
[1, 1, 2, 2]
```

### Hints for Problem 1

- Problem 1.2: [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__)
- Problem 1.3: [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__)
- Problem 1.4: [`__neg__()`](https://docs.python.org/3/reference/datamodel.html#object.__neg__)
- Problem 1.5: [`__add__()`](https://docs.python.org/3/reference/datamodel.html#object.__add__)
- Problem 1.6: [`__sub__()`](https://docs.python.org/3/reference/datamodel.html#object.__sub__)
- Problem 1.7: [`__mul__()`](https://docs.python.org/3/reference/datamodel.html#object.__mul__)
- Problem 1.8: [`__truediv__()`](https://docs.python.org/3/reference/datamodel.html#object.__truediv__), [`__floordiv__()`](https://docs.python.org/3/reference/datamodel.html#object.__floordiv__), [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented)

## 제출

답안을 따로 제출하지는 않고 각자 채점하기로 한다. 채점은 다음과 같이 할 수 있다.

    pytest -v test_homework2.py

`Vector` 클래스를 구현한 파일 이름은 `homework2.py` 로 한다.