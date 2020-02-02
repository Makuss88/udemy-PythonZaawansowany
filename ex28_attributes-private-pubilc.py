class Cake:

    def __init__(self, name, kind, taste, addictions, filling, gluten_free):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.filling = filling
        self.__gluten_free = gluten_free

    def showInfo(self):
        print('Gluten free?? - {}'.format(self.__gluten_free))


cake1 = Cake('vanilia', 'mniam', 'good', 'warm', 'better', True)
cake2 = Cake('muffin', 'muffin', ['chocolada', 'nuts'], 'cold', 'super', False)

#cake1.__gluten_free = False
cake1._Cake__gluten_free = False

print(vars(cake1))
print(vars(cake2))