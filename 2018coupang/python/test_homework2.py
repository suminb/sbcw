import pytest

from homework2 import Range, Vector


@pytest.mark.parametrize('n', range(2, 100, 17))
def test_problem1_1(n):
    v = Vector(*list(range(n)))


def test_problem1_1_invalid():
    with pytest.raises(ValueError):
        v = Vector()
    with pytest.raises(ValueError):
        v = Vector(1)


@pytest.mark.parametrize('xs, expected', [
    ([97, 53, 5, 33, 65, 62, 51, 100], '[97, 53, 5, 33, 65, 62, 51, 100]'),
    ([1.0, 2.5, 3.8], '[1.0, 2.5, 3.8]'),
    (['a', 'b', 'c'], '[a, b, c]'),
])
def test_problem1_2(xs, expected):
    v = Vector(*xs)
    assert str(v) == expected


@pytest.mark.parametrize('n', range(2, 100, 17))
def test_problem1_3(n):
    v = Vector(*list(range(n)))
    assert len(v) == n


@pytest.mark.parametrize('xs, expected', [
    ([76, 49, 40], [-76, -49, -40]),
    ([4, 10, 89, 69], [-4, -10, -89, -69]),
    ([77, 70, 75, 36, 56], [-77, -70, -75, -36, -56]),
    ([90, 67, 35, 66, 30, 27, 86, 75], [-90, -67, -35, -66, -30, -27, -86, -75]),
    ([75, 80, 42, 24, 31, 2, 93, 34, 14], [-75, -80, -42, -24, -31, -2, -93, -34, -14]),
])
def test_problem1_4(xs, expected):
    v = Vector(*xs)
    assert -v == Vector(*expected)
    assert -(-v) == Vector(*xs)


@pytest.mark.parametrize('xs, ys, expected', [
    ([100, 18], [5, 73], [105, 91]),
    ([50, 11, 47], [4, 77, 2], [54, 88, 49]),
    ([23, 91, 15, 61], [93, 7, 86, 2], [116, 98, 101, 63]),
    ([79, 12, 33, 8, 28], [82, 38, 44, 55, 23], [161, 50, 77, 63, 51]),
    ([64, 59, 5, 76, 12, 89], [25, 33, 45, 93, 60, 72], [89, 92, 50, 169, 72, 161]),
])
def test_problem1_5(xs, ys, expected):
    u, v = Vector(*xs), Vector(*ys)
    assert u + v == Vector(*expected)


def test_problem1_5_invalid():
    u, v = Vector(1, 2), Vector(1, 2, 3)
    with pytest.raises(ValueError):
        w = u + v


@pytest.mark.parametrize('xs, ys, expected', [
    ([89, 86], [98, 7], [-9, 79]),
    ([20, 43, 67], [15, 76, 56], [5, -33, 11]),
    ([1, 60, 87, 52], [83, 45, 49, 84], [-82, 15, 38, -32]),
    ([19, 71, 88, 1, 58], [42, 94, 5, 69, 35], [-23, -23, 83, -68, 23]),
    ([30, 97, 61, 45, 78, 36], [75, 81, 79, 16, 91, 39], [-45, 16, -18, 29, -13, -3])
])
def test_problem1_6(xs, ys, expected):
    u, v = Vector(*xs), Vector(*ys)
    assert u - v == Vector(*expected)


def test_problem1_6_invalid():
    u, v = Vector(1, 2), Vector(1, 2, 3)
    with pytest.raises(ValueError):
        w = u - v


@pytest.mark.parametrize('xs, n, expected', [
    ([-92, 2], 79, [-7268, 158]),
    ([97, 69, 81], -89, [-8633, -6141, -7209]),
    ([14, -84, -34, 79], -60, [-840, 5040, 2040, -4740]),
    ([35, 24, 43, 54, 93], -100, [-3500, -2400, -4300, -5400, -9300]),
    ([26, -17, -21, 19, -88, 6], -52, [-1352, 884, 1092, -988, 4576, -312]),
])
def test_problem1_7_scalar(xs, n, expected):
    v = Vector(*xs)
    assert v * n == Vector(*expected)


@pytest.mark.parametrize('xs, ys, expected', [
    ([100, -23], [22, -9], 2407),
    ([49, -45, 29], [-65, -28, -65], -3810),
    ([93, -76, 58, -36], [36, 80, 54, -63], 2668),
    ([-21, -75, 86, -82, 75], [-16, 20, 43, -75, -10], 7934),
    ([11, -20, 56, 63, -48, 41], [22, 13, 33, -34, -85, 40], 5408),
])
def test_problem1_7_dot_product(xs, ys, expected):
    u, v = Vector(*xs), Vector(*ys)
    assert u * v == expected


def test_problem1_7_invalid():
    u, v = Vector(1, 2), Vector(1, 2, 3)
    with pytest.raises(ValueError):
        w = u * v


@pytest.mark.parametrize('xs, n, expected', [
    ([-38, -96], 8.7, [-4.367816091954023, -11.03448275862069]),
    ([-31, -71, 80], -4.4, [7.045454545454545, 16.136363636363637, -18.18181818181818]),
    ([-5, -57, -15, 9], -8.5, [0.5882352941176471, 6.705882352941177, 1.7647058823529411, -1.0588235294117647]),
    ([-75, 100, -63, 78, -44], -8.9, [8.42696629213483, -11.235955056179774, 7.078651685393258, -8.764044943820224, 4.943820224719101]),
    ([46, 62, 36, 54, 74, -82], -9.4, [-4.8936170212765955, -6.595744680851063, -3.829787234042553, -5.74468085106383, -7.872340425531915, 8.72340425531915]),
])
def test_problem1_8_truediv(xs, n, expected):
    v = Vector(*xs)
    assert v / n == Vector(*expected)


@pytest.mark.parametrize('xs, n, expected', [
    ([-95, -51], -53, [1, 0]),
    ([83, -69, 22], -47, [-2, 1, -1]),
    ([86, -85, 73, -95], 39, [2, -3, 1, -3]),
    ([8, 58, -75, -34, -83], -44, [-1, -2, 1, 0, 1]),
    ([-82, 65, -23, -11, 11, -54], -85, [0, -1, 0, 0, -1, 0]),
])
def test_problem1_8_floordiv(xs, n, expected):
    v = Vector(*xs)
    assert v // n == Vector(*expected)


def test_problem1_8_invalid():
    u, v = Vector(1, 2), Vector(1, 2, 3)
    with pytest.raises(TypeError):
        w = u / v
    with pytest.raises(TypeError):
        w = u // v


@pytest.mark.parametrize('start, end', [
    (0, 0),
    (1, 2),
    (-10, 5),
    (-20, 0),
    (-30, -10),
])
def test_range_1(start, end):
    assert list(Range(start, end)) == list(range(start, end))


@pytest.mark.parametrize('start, end, step', [
    (0, 0, 1),
    (1, 2, 1),
    (3, 20, 1),
    (-10, 10, 3),
    (-10, 20, 100),
])
def test_range_2(start, end, step):
    assert list(Range(start, end, step)) == list(range(start, end, step))


@pytest.mark.parametrize('start, end, step', [
    (0, 0, 1),
    (1, 2, 1),
    (3, 20, 1),
    (-10, 10, 3),
    (-10, 20, 100),
])
def test_range_3(start, end, step):
    assert list(reversed(Range(start, end, step))) == list(reversed(range(start, end, step)))


def test_ragne_4():
    with pytest.raises(ValueError):
        _ = Range(0, 0, 0)