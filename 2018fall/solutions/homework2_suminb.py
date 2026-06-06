class DictWrapper(dict):

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def injective(self):
        return len(self.keys()) == len(set(self.values()))

    def invert(self):
        if self.injective():
            return self.__class__({v: k for k, v in self.items()})
        else:
            raise ValueError('Dictionary is not injective, hence cannot be inverted')


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