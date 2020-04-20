Cake1 = {'taste': 'vanilia',
         'glaze': 'chocolade',
         'text': 'Happy Brithday',
         'weight': 0.7
}

Cake2 = {'taste': 'tee',
         'glaze': 'lemon',
         'text': 'Happy Python Coding',
         'weight': 1.3
}


def show_cake_info(aCake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        aCake['taste'], aCake['glaze'], aCake['text'], aCake['weight'],))


show_cake_info(Cake1)
show_cake_info(Cake2)
print('-'*30)

cakes = [Cake1,Cake2]
for c in cakes:
    (show_cake_info(c))

