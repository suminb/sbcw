

class Series(object):

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.current = lower_bound

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.upper_bound:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1  # C/C++처럼 `return self.current++` 표현을 사용할 수 있었다면...


class Session(object):

    def __init__(self):
        self.connected = False

    def __enter__(self):
        print('__enter__')
        self.open()

    def __exit__(self, type, value, traceback):
        print('__exit__')
        self.close()

    def open(self):
        self.connected = True

    def close(self):
        self.connected = False

    def execute(self, query):
        if self.connected:
            print('Query has been executed')
        else:
            raise RuntimeError('Session is not active')


# s = Session()
# s.open()
# s.execute('SELECT * FROM ...')
# s.close()

# with s:
#     s.execute('SELECT ...')




# class Tetrapod:
#     pass

# class Amniota(Tetrapod):
#     pass

# class Mammal(Amniota):
#     pass



class Meta(type):

    def __new__(cls, name, bases, attrs):
        return super().__new__(cls, name, bases, attrs)


class Cat(metaclass=Meta):

    def __init__(self, name):
        self.name = name






if __name__ == '__main__':
    may = Cat('May')
