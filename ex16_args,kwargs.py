def calculate_paint(efficency_ltr_per_m2, *rooms):
    total_area = sum(rooms)
    return total_area * efficency_ltr_per_m2


m2 = 4

print(calculate_paint(m2, 1, 2, 15))

rooms = [1,2,15]
print(calculate_paint(m2, *rooms))


def log_it(*args):
    path = r'C:\Users\Blu\projects\udemy\txt16.txt'
    with open(path, "a") as f:
        for line in args:
            f.write(line)
            f.write(' ')

        f.write("\n")
    f.close()


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')