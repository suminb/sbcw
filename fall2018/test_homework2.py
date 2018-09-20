import math
import os
import random
import re

import pytest


random.seed(0)
solution = None
list_length = (5, 25)


@pytest.fixture
def random_word():
    def make(min_length=2, max_length=10):
        min_, max_ = ord('a'), ord('z')
        length = random.randint(min_length, max_length)
        return ''.join([chr(random.randint(min_, max_)) for _ in range(length)])
    return make


@pytest.fixture
def random_keys(random_word):
    def make(size=8):
        return [random_word() for _ in range(size)]
    return make


@pytest.fixture
def random_dict():
    def make(keys):
        return {k: random.randint(0, 1000) for k in keys}
    return make


def setup_module(module):
    username = pytest.config.getoption('username')
    solution_module = f'solution2_{username}'

    global solution
    try:
        solution = __import__(solution_module)
    except ImportError:
        pytest.exit(f'{solution_module}.py does not exist')


@pytest.mark.parametrize('_', range(8))
def test_dict_wrapper_1(random_keys, random_dict, _):
    keys = random_keys()
    d = solution.DictWrapper(random_dict(keys))

    for key in keys:
        assert d[key] == getattr(d, key)


def test_dict_wrapper_2():
    d = solution.DictWrapper({'key': 'value'})

    d['key'] = 'value2'
    assert d['key'] == 'value2'
    assert d.key == 'value2'

    d.key = 'value3'
    assert d['key'] == 'value3'
    assert d.key == 'value3'


@pytest.mark.parametrize('dict_, injective', [
    ({}, True),
    ({'wpn': 599, 'jk': 795, 'fusm': 170, 'czc': 441, 'xhbma': 196, 'mrq': 367, 'opzswv': 117, 'nclhi': 65}, True),
    ({'xw': 345, 'wuounlrfg': 861, 'sjaeeikk': 817, 'wckytbb': 999, 'ejdpxhbjfq': 351, 'jmk': 127, 'nddrpp': 490}, True),
    ({'wjmx': 561, 'ucatgwkf': 986, 'huomw': 742, 'bmwsnyvw': 85, 'fo': 857, 'iwf': 742}, False),
    ({'tvcadugtsd': 71, 'cldbtagf': 71, 'pgx': 71, 'va': 226}, False),

])
def test_dict_wrapper_3(dict_, injective):
    d = solution.DictWrapper(dict_)
    assert d.injective() == injective
 

@pytest.mark.parametrize('original, inverted, injective', [
    ({}, {}, True),
    ({'wpn': 599, 'jk': 795, 'fusm': 170, 'czc': 441, 'xhbma': 196, 'nclhi': 65},
     {599: 'wpn', 795: 'jk', 170: 'fusm', 441: 'czc', 196: 'xhbma', 65: 'nclhi'}, True),
    ({'xw': 345, 'wuounlrfg': 861, 'sjaeeikk': 817, 'wckytbb': 999},
     {345: 'xw', 861: 'wuounlrfg', 817: 'sjaeeikk', 999: 'wckytbb'}, True),
    ({'huomw': 742, 'bmwsnyvw': 85, 'fo': 857, 'iwf': 742}, None, False),
    ({'tvcadugtsd': 71, 'cldbtagf': 71, 'pgx': 71, 'va': 226}, None, False),

])
def test_dict_wrapper_4(original, inverted, injective):
    if injective:
        d = solution.DictWrapper(original)
        assert d.invert() == inverted
    else:
        with pytest.raises(ValueError):
            d = solution.DictWrapper(original)
            d.invert()