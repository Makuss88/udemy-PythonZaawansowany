import pickle
import glob

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

    def save_to_file(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)

        cls.list_Cake.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(catalog):
        return glob.glob(catalog + '/*.bakery')


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False)
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False)
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True)

cake01.save_to_file(r'C:\Users\Blu\projects\udemy\cake01.bakery')
cake02.save_to_file(r'C:\Users\Blu\projects\udemy\cake02.bakery')

cake05 = Cake.read_from_file(r'C:\Users\Blu\projects\udemy\cake01.bakery')
cake05.show_info()

print(Cake.get_bakery_files(r'C:\Users\Blu\projects\udemy'))