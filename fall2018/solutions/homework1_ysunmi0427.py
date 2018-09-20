# Problem 1
def square(xs):
    return [x ** 2 for x in xs]

def even(xs):
    return [x for x in xs if x % 2 == 0]

# Problem 2
def convert(text):
    # return text.replace(',', '@gmail.com;') + '@gmail.com'
    return '; '.join([x + '@gmail.com' for x in text.split(', ')])

# Problem 3
def intersection(xs, ys):
    return [x for x in xs if x in ys]

def union(xs, ys):
    return [x for x in xs if x not in ys] + ys

# Problem 4
def net_asset_value(inventory, prices):
    return sum([inventory[i] * prices[i] for i in inventory.keys()])

# Problem 5
def invert(index):
    # return {index[k]:k for k in index.keys()}
    return {v: k for k, v in index.items()} # items()는 (key, value) 튜플을 줌

# Problem 6
def zip(*args):
    return [tuple([a[i] for a in args]) for i in range(min(len(l) for l in args))]

def unzip(iterables):
    return [tuple([i[l] for i in iterables]) for l in range(min(len(i) for i in iterables))]
