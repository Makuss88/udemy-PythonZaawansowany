import time
import functools


def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        time_start = time.time()
        result = a_function(*args, **kwargs)
        time_stop = time.time()
        timer = time_stop-time_start
        print("Function: {} - time: {}".format(a_function.__name__, timer))

        return result

    return a_wrapped_function


#@wrapper_time
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


#print(get_sequence(3))

GetWithLog = wrapper_time(get_sequence)
print(GetWithLog(18))

# ja wole bez dekoratora...