class DictWrapper(object):

    def __init__(self, dict_):
        self.dict_ = dict_

    def __getattr__(self, key):
        return self.dict_[key]

    def __getitem__(self, key):
        return self.dict_[key]

class DictWrapper(object):

    def __init__(self, dict_):
        self.dict_ = dict_

    def __setattr__(self, key, value):
        self.dict_[key] = value

    def __getattr__(self, key):
        return self.dict_[key]

    def __setitem__(self, key, value):
        self.dict_[key] = value

    def __getitem__(self, key):
        return self.dict_[key]

    dict_ = {}


class DictWrapper(object):
    def __init__(self, dict_):
        self.dict_ =  dict_

    def __getattr__(self, key):
        return self.dict_['key']

    def __getitem__(self, key):
        return self.dict_['key']

    def __len__(self):
        return len(self.dict_)

    def injective(self):
            if len(set(self.dict_.keys())) != len(set(self.dict_.values())):
                return False
            else:
                return True

class DictWrapper(object):
    def __init__(self, dict_):
        self.dict_ =  dict_

    def __getattr__(self, key):
        return self.dict_['key']

    def __getitem__(self, key):
        return self.dict_['key']

    def __len__(self):
        return len(self.dict_)

    def invert(self):
        if len(set(self.dict_.keys())) == len(set(self.dict_.values())):
            self.dict_ = {x:y for x, y in self.dict_.items()}
            return self.dict_
        else:
            raise ValueError

class Range(object):
    def __init__(self, start, end, interval):
        self.start = start
        self.end = end
        self.interval = interval

    def __iter__(self):
        return self

    def __next__(self):
        if self.interval == 0:
            raise ValueError

        if self.start < self.end:
            x = self.start
            self.start += self.interval
            return x
        else:
            raise StopIteration


class Range(object):
    def __init__(self, start, end, interval=None):
        self.start = start
        self.end = end
        self.interval = interval if interval is not None else 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.interval == 0:
            raise ValueError

        if self.start < self.end:
            x = self.start
            self.start += self.interval
            return x
        else:
            raise StopIteration

    def __reversed__(self):
        return reversed(list(self))
