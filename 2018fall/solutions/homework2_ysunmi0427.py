import math

# Problem 1
# Problem 1.1
# class DictWrapper(object):
#     def __init__(self, dict_):
#         self.d = dict_

#     def __getattr__(self, key):
#         return self.d[key]

#     def __getitem__(self, key):
#         return self.d[key]

# Simpler way
class DictWrapper(dict):
    # Problem 1.1
    def __getattr__(self, key):
        # return self.__getitem__(key)
        return self[key]
    
    # Problem 1.2
    def __setattr__(self, key, value):
        self[key] = value 

    # Problem 1.3
    def injective(self):
        return len(self.keys()) == len(set(self.values()))

    # Problem 1.4
    def invert(self):
        if self.injective():
            return DictWrapper({v:k for k, v in self.items()})
        else:
            raise ValueError('Dictionary is not injective, hence cannot be inverted')

# Problem 2
# class Range(object):
#     # Problem 2.1
#     def __init__(self, start, stop, step=1):
#         self.start = start
#         self.stop = stop
#         self.step = step
#         self.current = start
#         if step == 0:
#             raise ValueError('`step` cannot be zero')
#     def __iter__(self):
#         return self
#     def __next__(self):
#         # Assumption of this approach: start is always smaller than stop
#         if self.current >= self.stop:
#             raise StopIteration
#         else:
#             self.current += self.step
#             return self.current - self.step
#     # Problem 2.2
#     def __reversed__(self):
#         return reversed(list(Range(self.start, self.stop, self.step)))

# Problem 2
class Range(object):
    # Problem 2.1
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start
        if step == 0:
            raise ValueError('`step` cannot be zero')
    def __iter__(self):
        return self
    def __next__(self):
        # Generalized version
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        else:
            self.current += self.step
            return self.current - self.step
  
    # Problem 2.2
    def __reversed__(self):
        # simpler than below but.. lol
        # return reversed(list(Range(self.start, self.stop, self.step)))
        length = math.ceil((self.stop - self.start) / self.step)
        return Range(self.start + self.step * (length-1), self.start-1, -self.step)