def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


def generate_values(how, number):
    result = []

    for x in number:
        result.append(how(x))

    return result


number = list(range(11))

print(generate_values(double, number))
print(generate_values(root, number))
print(generate_values(negative, number))
print(generate_values(div2, number))