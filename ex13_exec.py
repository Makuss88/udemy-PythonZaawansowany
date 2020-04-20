files_to_process = [
    r'C:\Users\Blu\projects\udemy\ex13a.py',
    r'C:\Users\Blu\projects\udemy\ex13b.py'
    ]

counter = 0

for file_path in files_to_process:
    counter += 1
    print('Process', counter)
    with open(file_path, 'r') as f:
        source = f.read()
        exec(source)