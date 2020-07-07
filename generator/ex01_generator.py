def Combinations(products, promotions, customers):
    for prod in products:
        for prom in promotions:
            for cust in customers:
                yield '{}, {}, {}'.format(prod, prom, cust)


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

for c in Combinations(products, promotions, customers):
    print(c)
