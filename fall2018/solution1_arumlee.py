def square(xs):
    return [i ** 2 for i in xs]

def even(xs):
    return [i for i in xs if i % 2 == 0]

def convert(text):
    text = text.split(', ')
    text = "@gmail.com; ".join(text)
    text = text + '@gmail.com'
    return text

def intersection(xs, ys):
    pass

def union(xs, ys):
    pass

def net_asset_value(inventory, prices):
    pass


