def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 8

transformations = [double, root, negative, div2]
transformations2 = [root,root,div2,double]

for tran in transformations:
    print('{}: temporal result is {}'.format(tran.__name__, tran(number)))
