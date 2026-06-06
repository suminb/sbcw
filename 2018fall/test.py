def parent():
    print('Printing from the parent() function')

    def first_child():
        print('Printing from the first_child() function')

    return first_child


if __name__ == '__main__':
    pass
