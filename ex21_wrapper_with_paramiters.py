import os, functools
from datetime import datetime as dt

def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            file = open(log_file_path, "a")
            file.write('-'*50 + "\n")
            file.write('Function {} in {} - time is: {}'.format(logged_action, path, dt.now().strftime("%Y-%m-%d %H:%M:%S")))
            file.write("\n")
            file.close()
            result = func(path)
            return result
        return the_real_wrapper
    return wrapper_with_log_to_known_file

@wrapper_with_log_file('FILE CREATED', r'C:\Users\Blu\projects\udemy\txt1.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")

@wrapper_with_log_file('FILE DELETED', r'C:\Users\Blu\projects\udemy\txt2.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')
create_file(r'c:\temp\dummy_file.txt')

