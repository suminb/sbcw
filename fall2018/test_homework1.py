def convert(text):
    pass


def test_problem1():
    text = 'alejandro, britney, christina, dennis, emily'
    expected = \
        'alejandro@gmail.com; britney@gmail.com; christina@gmail.com; ' \
        'dennis@gmail.com; emily@gmail.com'
    assert convert(text) == expected