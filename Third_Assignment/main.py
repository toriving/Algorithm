import rbtree

def read_file(PATH = 'input.txt'):
    # If you have an input.txt file in folder, you can easily get results via this function.

    dic = dict({'I': t.insert, 'D': t.delete, 'R': t.report, 'C': t.count, 'P': t.print, 'E': False})
    f = open(PATH)
    for line in f.readlines():
        if line[0] == 'E':
            exit()
        line = line.split()
        dic[line[0]](*line[1:])
        if line[0] == 'I':
            print('Insert', line[1])
        elif line[0] == 'D':
            print('Delete', line[1])
        print('='*20)


if __name__ == '__main__':
    t = rbtree.Augmented_Red_Black_Tree()
    read_file()

"""
    t.insert(20)
    t.insert(29)
    t.insert(38)
    t.insert(27)
    t.insert(12)
    t.insert(23)
    t.insert(25)
    t.insert(21)
    t.insert(17)
    t.insert(15)
    print(t)
    t.report(17, 27)
    print('-'*20)
    t.count(17, 27)
    print('-' * 20)
    t.report(21, 29)
    print('-' * 20)
    t.count(21, 29)
    print('-' * 20)
    print(t)
    t.delete(25)
    print(t)
    t.insert(25)
    t.insert(22)
    print(t)
    t.report(21, 29)
    print('-' * 20)
    t.count(21, 29)
    print('-' * 20)
    t.report(17, 21)
    print('-' * 20)
    t.count(17, 21)
    print('-' * 20)
    t.delete(20)
    t.delete(25)
    t.delete(27)
    t.delete(38)
    t.delete(29)
    print(t)
    t.report(12, 22)
    print('-' * 20)
    t.count(12, 22)
    print('-' * 20)
    t.report(17, 21)
    print('-' * 20)
    t.count(17, 21)
    print('-' * 20)
"""