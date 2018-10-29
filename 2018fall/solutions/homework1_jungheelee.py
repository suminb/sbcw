# Problem 1.1
def square(xs):
    return [x * x for x in xs]


# Problem 1.2
def even(xs):
    return [x for x in xs if x % 2 == 0]


# Problem 2
def convert(text):
    return '; '.join([x.strip() + '@gmail.com' for x in text.split(',')])


# Problem 3.1
def intersection(xs, ys):
    return [x for x in xs if x in ys]


# Problem 3.2
def union(xs, ys):
    return xs + [y for y in ys if y not in xs]


# Problem 4
def net_asset_value(inventory, prices):
    return sum(prices[item] * quantity for item, quantity in inventory.items())


# Problem 5
def invert(index):
    return {val: it for it, val in zip(index.keys(), index.values())}


# Homework 6.1 (Bonus)
def zip(*args):
    # 여기에 여러분의 코드를 작성하세요
    pass


# Homework 6.2 (Bonus)
def unzip(iterable):
    # 여기에 여러분의 코드를 작성하세요
    pass
