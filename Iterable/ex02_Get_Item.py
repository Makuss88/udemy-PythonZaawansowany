import sys


class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

    def __getitem__(self, item):
        if item >= len(self.products) * len(self.customers) * len(self.promotions):
            raise StopIteration
        else:
            pos_products = item // (len(self.promotions) * len(self.customers))
            item = item % (len(self.promotions) * len(self.customers))

            pos_promotions = item // len(self.customers)
            item = item % len(self.customers)

            pos_customers = item

        item_to_return = "{} - {} -{}".format(self.products[pos_products],
                                              self.promotions[pos_promotions],
                                              self.customers[pos_customers])
        return item_to_return


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)

comb = iter(combinations)
# count = 0  #  we must counter from 0!
# for i in comb:
#     print(count, i)
#     count += 1

# print(sys.getsizeof(comb))
try:
    for i in range(0, 31):
        print(i, combinations[i])
except:
    print('Error:', StopIteration)
