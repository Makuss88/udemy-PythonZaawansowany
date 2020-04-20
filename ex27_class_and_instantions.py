class Cake:
    
    def __init__(self, name, kind, taste, addictions, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.filling = filling


cake1 = Cake('vanilia', 'mniam', 'good', 'warm', 'better')
cake2 = Cake('muffin', 'muffin', ['chocolada', 'nuts'], 'cold', 'super')


listCakes = [cake1,cake2]

for l in listCakes:
    print(l.name, l.kind, l.taste, l.addictions, l.filling)