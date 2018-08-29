def convert(text):
    return "@gmail.com; ".join(map(lambda s: s.strip(), text.split(',')))+"@gmail.com"
