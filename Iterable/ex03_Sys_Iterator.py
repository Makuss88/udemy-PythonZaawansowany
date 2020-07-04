import csv

with open('./data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))

    # print(next(csvfile))
    # print(next(csvfile))
    # print(next(csvfile))
    # print(next(csvfile))
    # print(next(csvfile))

    while True:
        try:
            print(next(csvfile))
        except StopIteration:
            break
    print('All lines have been shown to You. JAHU!')