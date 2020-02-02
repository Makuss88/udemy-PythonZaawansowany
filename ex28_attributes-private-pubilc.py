class Cake:

    list_Cake = []

    def __init__(self, name, kind, taste, addictions, filling, gluten_free):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.filling = filling
        self.__gluten_free = gluten_free
        self.list_Cake.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.addictions) > 0:
            print("Additives:")
            for a in self.addictions:
                print("\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print("Gluten free: {}".format(self.__gluten_free))
        print('-' * 20)


cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False)
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False)
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '', True)

# cake1.__gluten_free = False
cake01._Cake__gluten_free = False

for c in Cake.list_Cake:
    c.show_info()

print(dir(cake03))