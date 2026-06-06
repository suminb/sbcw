class Vector:

    def __init__(self, *elements):
        self.elements = elements

    def __eq__(self, other):
        return all([x == y for x, y in zip(self.elements, other.elements)])

    def __repr__(self):
        return 'Vector(' + ', '.join([str(x) for x in self.elements]) + ')'

    def __len__(self):
        return len(self.elements)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(*[x + y for x, y in
                            zip(self.elements, other.elements)])
        else:
            raise TypeError('...')

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*[x / other for x in self.elements])
        else:
            raise TypeError('...')


def f(x, input_):
    return x + 1


if __name__ == '__main__':
    # globals()['g'] = lambda x: x + 2
    # print(f(1))
    # print(g(1))

    list = [1, 2, 3]
    xs = list([2, 3])

    print(xs)

