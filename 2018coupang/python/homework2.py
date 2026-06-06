def is_scalar(value):
    return not hasattr(value, '__len__')

class Vector:
    def __init__(self, *elements):
        if len(elements) < 2:
            raise ValueError('At least two elements are required')
        self.elements = elements
        self.size = len(elements)

    def __eq__(self, other):
        return all([x == y for x, y in zip(self.elements, other.elements)])

    def __repr__(self):
        return '[' + ', '.join(map(str, self.elements)) + ']'

    def __len__(self):
        return len(self.elements)

    def __neg__(self):
        return Vector(*[-x for x in self.elements])

    def __add__(self, other):
        self._check_size(other)
        return Vector(*[x + y for x, y in zip(self.elements, other.elements)])

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        if is_scalar(other):
            return Vector(*[other * x for x in self.elements])
        elif isinstance(other, Vector) or hasattr(other, '__len__'):
            self._check_size(other)
            return sum([x * y for x, y in zip(self.elements, other.elements)])
        else:
            raise NotImplementedError

    def __truediv__(self, other):
        if is_scalar(other):
            return Vector(*[x / other for x in self.elements])
        else:
            return NotImplemented

    def __floordiv__(self, other):
        if is_scalar(other):
            return Vector(*[x // other for x in self.elements])
        else:
            return NotImplemented

    def _check_size(self, other):
        if len(self) != len(other):
            raise ValueError(f'A vector of size {len(self)} is expected')


class Range:

    def __init__(self, start, end, step=1):
        if step == 0:
            raise ValueError('`step` cannot be zero')
        self.start = start
        self.end = end
        self.step = step
        self.curr = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr >= self.end:
            raise StopIteration
        else:
            self.curr += self.step
            return self.curr - self.step

    def __reversed__(self):
        _ = 0
        try:
            while True:
                _ += next(self)
        except StopIteration:
            pass

        while self.curr > self.start:
            self.curr -= self.step
            yield self.curr