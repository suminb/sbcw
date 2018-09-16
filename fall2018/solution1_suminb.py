def square(xs):
    return [x * x for x in xs]


def even(xs):
    return [x for x in xs if x % 2 == 0]


def convert(text):
    return '; '.join([x.strip() + '@gmail.com' for x in text.split(',')])


def intersection(xs, ys):
    return [x for x in xs if x in ys]


def union(xs, ys):
    return xs + [y for y in ys if y not in xs]


def net_asset_value(inventory, prices):
    return sum(prices[item] * quantity for item, quantity in inventory.items())


def invert(index):
    return {v: k for k, v in index.items()}


def zip(*iterables):
    return [tuple(x[j] for x in iterables) for j in range(min(len(i) for i in iterables))]


def unzip(iterable):
    return zip(*iterable)
