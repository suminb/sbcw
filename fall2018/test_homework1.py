import math
import os
import random
import re

import pytest


random.seed(0)
solution = None
list_length = (5, 25)


def setup_module():
    solution_files = [fn for fn in os.listdir() if re.match(r'solution1_\w+\.py', fn)]
    assert len(solution_files) > 0, 'Could not find any solution'

    module_name = solution_files[0][:-3]

    global solution
    solution = __import__(module_name)


@pytest.mark.parametrize('i', range(10))
def test_problem1_1(i):
    xs = random.sample(range(100), random.randint(*list_length))
    # NOTE: We decided to call `sqrt()` so that we don't leak the solution for this problem
    assert all([float(x) == math.sqrt(y) for x, y in zip(xs, solution.square(xs))])


@pytest.mark.parametrize('i', range(10))
def test_problem1_2(i):
    xs = random.sample(range(100), random.randint(*list_length))
    assert all([x % 2 == 0 for x in solution.even(xs)])


def test_problem2():
    text = 'alejandro, britney, christina, dennis, emily'
    expected = \
        'alejandro@gmail.com; britney@gmail.com; christina@gmail.com; ' \
        'dennis@gmail.com; emily@gmail.com'
    assert solution.convert(text) == expected


@pytest.mark.parametrize('i', range(10))
def test_problem3_1(i):
    xs = random.sample(range(100), random.randint(*list_length))
    ys = random.sample(range(100), random.randint(*list_length))
    assert set(solution.intersection(xs, ys)) == set(xs).intersection(ys)


@pytest.mark.parametrize('i', range(10))
def test_problem3_2(i):
    xs = random.sample(range(100), random.randint(*list_length))
    ys = random.sample(range(100), random.randint(*list_length))
    assert set(solution.union(xs, ys)) == set(xs).union(ys)


@pytest.mark.parametrize('inventory, prices, nav', [
    ({}, {}, 0),
    (
        {'banana': 1000},
        {'banana': 0.90},
        900
    ),
    (
        {
            'avocado': 236,
            'apple': 0,
            'orange': 172,
            'mango': 368,
        },
        {
            'avocado': 0.99,
            'apple': 0.69,
            'orange': 0.33,
            'mango': 0.79
        },
        581.12
    )
])
def test_problem4(inventory, prices, nav):
    assert solution.net_asset_value(inventory, prices) == nav
