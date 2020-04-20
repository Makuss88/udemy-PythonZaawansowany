class NoDuplicates:

    def __init__(self, list):
        self.list_of_word = list

    def __call__(self, new_items):

        for n in new_items:
            if not n in self.list_of_word:
                self.list_of_word.append(n)


car = NoDuplicates([])

car('Opel')
car('Seat')
car('Fiat')

print(car.list_of_word)

print('-' * 40)

my_no_dup_list = NoDuplicates([])
list01 = ['Mouse', 'Key']
list02 = ['Pen', 'Mouse', 'Key']
list03 = ['Pen', 'Charger']

print(my_no_dup_list.list_of_word)

print('-' * 40)

my_no_dup_list(list01)
print(my_no_dup_list.list_of_word)

print('-' * 40)
my_no_dup_list(list02)
print(my_no_dup_list.list_of_word)

print('-' * 40)
my_no_dup_list(list03)
print(my_no_dup_list.list_of_word)
