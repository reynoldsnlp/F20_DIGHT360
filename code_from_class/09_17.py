for i in range(3):
    fname = 'file' + str(i) + '.txt'  # f'file{i}.txt'
    with open(fname, 'w') as each_file:
        print('This is', fname, file=each_file)


def add_two_ints(x, y):
    return x + y

add_two_ints(3, 5)
