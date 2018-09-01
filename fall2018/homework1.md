## Problem 1

이 문제는 여러개의 하위 문제로 구성된 문제입니다. 코드를 길게 작성해서 풀어도 상관 없지만, 파이썬의 [list comprehension](https://www.programiz.com/python-programming/list-comprehension)을 이용하면 단 한줄로 해결할 수 있는 문제들입니다.

## Problem 1.1

```python
def square(xs):
    # 여기에 여러분의 코드를 작성하세요
    pass
```

정수 리스트가 주어졌을 때 각 원소의 제곱을 가지는 새로운 리스트를 반환하는 함수를 작성하십시오.

    xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

예를 들어서, 위와 같은 리스트가 주어졌을 때 다음과 같은 리스트가 반환되어야 합니다.

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## Problem 1.2

```python
def even(xs):
    # 여기에 여러분의 코드를 작성하세요
    pass
```

임의의 정수 리스트가 주어졌을 때 짝수인 원소만 담고 있는 새로운 리스트를 반환하는 함수를 작성하십시오. 예를 들어서, 문제 1.1의 결과 리스트가 (`[1, 4, 9, 16, ...]`) 주어졌을 때 다음과 같은 리스트가 반환되어야 합니다.

    [4, 16, 36, 64, 100]

## Problem 2

친구들에게 단체 이메일을 보내려고 하는데, 이메일 주소 전체가 아닌 유저 이름 부분만 담긴 텍스트 파일이 주어졌습니다.

    alejandro, britney, christina, dennis, emily

유저 이름 뒤에 `@gmail.com`을 붙여야 하는데, 이걸 수동으로 하기에 우리 인생은 너무 짧습니다. 이것을 다음과 같이 변환하는 코드를 작성하십시오.

    alejandro@gmail.com; britney@gmail.com; christina@gmail.com; dennis@gmail.com; emily@gmail.com

여러분이 할 일은 `homework1.py`에 있는 `convert()` 함수를 구현하는 것입니다. `text`가 주어졌을 때 세미콜론(`;`)으로 구분된 이메일 주소들을 반환하는 함수입니다. 이 함수가 반환한 문자열을 이메일 주소 칸에 그대로 붙여넣으면 단체 메일을 보낼 수 있습니다.

```
def convert(text):
    # 여기에 여러분의 코드를 작성하세요
    pass
```

## Problem 3

3.1, 3.2는 `set`을 사용하지 않고 구현해봅시다.

## Problem 3.1

```python
def intersection(xs, ys):
    # 여기에 여러분의 코드를 작성하세요
    pass
```

다음과 같이 두 개의 정수 리스트가 주어졌을 때 두 리스트 모두에 존재하는 원소들만 반환하는 코드를 작성하십시오.

    xs = [5, 10, 15, 20, 25, 30, 35, 40]
    ys = [9, 2, 3, 8, 10, 5, 21, 7]

여러분이 작성할 함수는 인자를 두 개 받는 함수입니다. 기대되는 반환값은 다음과 같습니다.

    [5, 10]

## Problem 3.2

```python
def union(xs, ys):
    # 여기에 여러분의 코드를 작성하세요
    pass
```

두 개의 정수 리스트가 주어졌을 때 값이 중복되지 않도록 합치는 함수를 작성하십시오.

    xs = [1, 2, 3, 4]
    ys = [3, 4, 5, 6]

반환값의 순서는 관계 없습니다.

    [1, 2, 3, 4, 5, 6]

## Problem 4

```python
def net_asset_value(inventory, prices):
    # 여기에 여러분의 코드를 작성하세요
    pass
```

상품의 재고(`inventory`) 정보와 가격(`prices`) 정보가 주어졌을 때 총 재고 가치를 산출하는 함수를 작성하십시오.

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

위와 같은 경우 총 재고 가치는 `581.12` 입니다. 코드를 너무 복잡하게 만드는 것을 방지하기 위해서 `prices`는 항상 `inventory`에 있는 모든 아이템에 대한 가격 정보를 담고 있다고 가정해도 좋습니다.


## 제출

답안은 `solution1_(GitHub 아이디).py` 파일로 제출해주십시오. 예를 들어서, GitHub 사용자 이름이 `suminb`라고 가정한다면 파일 이름은 `solution1_suminb.py`가 되어야 합니다.

## 자동 채점

코드를 테스트 하기 위해서는 `pytest` 패키지가 필요합니다. 다음의 명령어를 실행하여 설치하도록 합니다.

    pip install pytest

패키지가 설치되면 다음과 같이 테스트 파일을 실행해서 여러분이 작성한 코드가 제대로 작동되는지 검증하도록 합니다.

    pytest -v test_homework1.py

## 참고할만한 자료

- https://www.datacamp.com/community/tutorials/data-structures-python
