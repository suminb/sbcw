import math
import os
import random
import re

import pytest


random.seed(0)
solution = None
list_length = (5, 25)


def setup_module(module):
    username = pytest.config.getoption('username')
    solution_module = f'homework1_{username}'

    try:
        namespace = __import__(f'solutions.{solution_module}')
    except ImportError:
        pytest.exit(f'{solution_module}.py does not exist')
    else:
        global solution
        solution = getattr(namespace, solution_module)


@pytest.fixture
def random_list():
    def make(min_len, max_len):
        return random.sample(range(100), random.randint(min_len, max_len))
    return make


@pytest.mark.parametrize('_', range(10))
def test_problem1_1(_, random_list):
    xs = random_list(*list_length)
    # NOTE: We decided to call `sqrt()` so that we don't leak the solution for
    # this problem
    assert all([float(x) == math.sqrt(y) for x, y in zip(xs, solution.square(xs))])


@pytest.mark.parametrize('_', range(10))
def test_problem1_2(_, random_list):
    xs = random_list(*list_length)
    assert all([x % 2 == 0 for x in solution.even(xs)])


def test_problem2():
    text = 'alejandro, britney, christina, dennis, emily'
    expected = \
        'alejandro@gmail.com; britney@gmail.com; christina@gmail.com; ' \
        'dennis@gmail.com; emily@gmail.com'
    assert solution.convert(text) == expected


@pytest.mark.parametrize('_', range(10))
def test_problem3_1(_, random_list):
    xs = random_list(*list_length)
    ys = random_list(*list_length)
    assert set(solution.intersection(xs, ys)) == set(xs).intersection(ys)


@pytest.mark.parametrize('_', range(10))
def test_problem3_2(_, random_list):
    xs = random_list(*list_length)
    ys = random_list(*list_length)
    assert set(solution.union(xs, ys)) == set(xs).union(ys)


@pytest.mark.parametrize('inventory, prices, nav', [
    ({}, {}, 0),
    (
        {'banana': 1000},
        {'banana': 0.90},
        900
    ),
    (
        {'avocado': 236, 'apple': 0, 'orange': 172, 'mango': 368},
        {'avocado': 0.99, 'apple': 0.69, 'orange': 0.33, 'mango': 0.79},
        581.12
    )
])
def test_problem4(inventory, prices, nav):
    assert solution.net_asset_value(inventory, prices) == nav


@pytest.mark.parametrize('index, inverted_index', [
    ({}, {}),
    (
        {'a': 1, 'b': 2, 'c': 3},
        {1: 'a', 2: 'b', 3: 'c'},
    ),
    (
        {'transparency': 37, 'composibility': 5, 'immutability': 40, 'idempotency': 14},  # noqa
        {37: 'transparency', 5: 'composibility', 40: 'immutability', 14: 'idempotency'},  # noqa
    )
])
def test_problem5(index, inverted_index):
    assert solution.invert(index) == inverted_index


@pytest.mark.parametrize('_', range(10))
def test_problem6_1(_, random_list):
    m = random.randint(1, 10)  # Number of lists
    lists = [random_list(0, 25) for _ in range(m)]
    assert list(zip(*lists)) == list(solution.zip(*lists))


@pytest.mark.parametrize('_', range(10))
def test_problem6_2(_, random_list):
    m = random.randint(1, 10)  # Number of lists
    lists = [random_list(0, 25) for _ in range(m)]
    assert list(zip(*lists)) == list(solution.unzip(lists))
