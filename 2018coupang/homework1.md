# Homework 1

List comprehension을 이용한다면 모두 한 줄로 해결할 수 있는 문제들이다. 여기서 *한 줄*이라 함은 문자 그대로 코드를 한 줄에 우겨 넣는 것이 중요한 것이 아니라 하나의 표현식(expression)으로 해결 가능하다는 것이 주안점이다. 가독성을 위해서라면 하나의 표현식을 여러 줄에 걸쳐 써도 무방하다.

참고: [List comprehension](https://www.programiz.com/python-programming/list-comprehension)으로 해결하기 어렵다면 먼저 `for`, `while` 등의 반복문으로 해결을 한 다음 다시 list comprehension 으로 해결해 보는 것을 추천한다.

참고: 문제를 단순화하기 위해서 입력값은 모두 올바른 값이 주어진다고 가정하고 진행해도 좋다. 예를 들어서, 하나 이상의 원소가 있어야 하는 문제에 빈 리스트가 주어지거나, 정수형 리스트를 기대하는 함수에 문자열이 주어지는 경우는 없다.

## Problem 1

```python
def square(xs):
    # Put your code here
    pass
```

정수 리스트가 주어졌을 때 각 원소의 제곱을 가지는 새로운 리스트를 반환하는 함수를 작성하여라. 다음과 같이 작동해야 한다.

```
>>> square([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## Problem 2

```python
def even(xs):
    # Put your code here
    pass
```

임의의 정수 리스트가 주어졌을 때 짝수인 원소만 담고 있는 새로운 리스트를 반환하는 함수를 작성하여라.

```
>>> even([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
[4, 16, 36, 64, 100]
```

## Problem 3

```python
def count_other_words(sentence, exclude):
    # Put your code here
    pass
```

주어진 문장에서 특정 단어를 제외한 나머지 단어의 개수를 세는 코드를 작성하여라. 리스트 원소의 합을 구할 때에는 `sum()` 함수를 쓰면 편리하다.

```
>>> count_other_words('the quick brown fox jumps over the lazy dog', 'the')
7
```

## Problem 4

```python
def delta(xs):
    # Put your code here
    pass
```

정수 또는 실수 원소를 가지는 리스트가 주어졌을 때 바로 이웃한 원소들간의 차를 구하는 코드를 작성하여라.

```
>>> delta([1, 2, 3, 4])
[1, 1, 1, 1]

>>> delta([4, 1, 1, 2, 4, 9])
[-3, 0, 1, 2, 5]
```

## Problem 5

5.1, 5.2는 `set`을 사용하지 않고 구현해보는 것이 목적이다.

### Problem 5.1

```python
def intersection(xs, ys):
    # Put your code here
    pass
```

다음과 같이 두 개의 정수 리스트가 주어졌을 때 두 리스트 모두에 존재하는 원소들만 반환하는 코드를 작성하여라.

```
>>> xs = [5, 10, 15, 20, 25, 30, 35, 40]
>>> ys = [9, 2, 3, 8, 10, 5, 21, 7]
>>> intersection(xs, ys)
[5, 10]
```

### Problem 5.2

```python
def union(xs, ys):
    # Put your code here
    pass
```

두 개의 정수 리스트가 주어졌을 때 값이 중복되지 않도록 합치는 함수를 작성하여라.

```
>>> xs = [1, 2, 3, 4]
>>> ys = [3, 4, 5, 6]
>>> union(xs, ys)
[1, 2, 3, 4, 5, 6]
```

반환값의 순서는 관계 없다.

## Problem 6

```python
def net_asset_value(inventory, prices):
    # Put your code here
    pass
```

상품의 재고(`inventory`) 정보와 가격(`prices`) 정보가 주어졌을 때 총 재고 가치를 산출하는 함수를 작성하여라.

```python
inventory = {
    'avocado': 236,
    'apple': 0,
    'orange': 172,
    'mango': 368,
}

prices = {
    'avocado': 0.99,
    'apple': 0.69,
    'orange': 0.33,
    'mango': 0.79
}
```

위와 같은 경우 총 재고 가치는 `581.12` 이다. 코드를 너무 복잡하게 만드는 것을 방지하기 위해서 `prices`는 항상 `inventory`에 있는 모든 아이템에 대한 가격 정보를 담고 있다고 가정해도 좋다.

```
>>> net_asset_value(inventory, prices)
581.12
```

## Problem 7

```python
def is_monotonic(xs):
    # Put your code here
    pass
```

주어진 리스트의 monotonic 여부를 판단하는 코드를 작성하여라. Monotonic 리스트는 다음 두 가지 조건 중 하나를 만족하는 리스트이다.

- Non-increasing: 원소의 값이 증가하지 않음 (같거나 감소함, *a<sub>i</sub> &ge; a<sub>i+1</sub>*)
- Non-decreasing: 원소의 값이 감소하지 않음 (같거나 증가함, *a<sub>i</sub> &le; a<sub>i+1</sub>*)

```
>>> is_monotonic([1, 2, 3, 4])
True

>>> is_monotonic([4, 3, 2, 1])
True

>>> is_monotonic([0, 0, 0, 0])
True

>>> is_monotonic([1, 2, 1, 2])
False
```

## 제출

코드를 제출하는 방법에 대해서는 아직 고민중이다. `#python_seminar` 채널을 통해서 공지할 예정이다.