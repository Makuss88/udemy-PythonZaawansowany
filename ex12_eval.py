import math
'''
2*x

math.sin(x)

3*x**2+2*x-4
'''

argument_list = []
formula = 'math.sin(x)'

for i in range(100):
    argument_list.append(i / 10)

for x in argument_list:
    print("{0:3.1f} {1:6.3f}".format(x, eval(formula)))