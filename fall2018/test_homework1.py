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
    assert set(solution.intersect(xs, ys)) == set(xs).intersection(ys)


@pytest.mark.parametrize('i', range(10))
def test_problem3_2(i):
    xs = random.sample(range(100), random.randint(*list_length))
    ys = random.sample(range(100), random.randint(*list_length))
    assert set(solution.union(xs, ys)) == set(xs).union(ys)
