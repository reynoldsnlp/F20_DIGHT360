for i in range(3):
    fname = 'file' + str(i) + '.txt'  # f'file{i}.txt'
    with open(fname, 'w') as each_file:
        print('This is', fname, file=each_file)