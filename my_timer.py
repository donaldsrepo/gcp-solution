"""
Application to provide benchmark timers for code. 
Usage: 
# from my_timer_class import MyTimer
from my_timer_func import my_timer
import time

@MyTimer3(name="decorator")
@my_timer
"""

import functools
import time

def my_timer(orig_func):
    import time
    @functools.wraps(orig_func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = orig_func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time to run {orig_func.__name__}: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer


class MyTimer():
    # usage:
    #
    # from MyTimer import MyTimer
    # with MyTimer():
    #    func(x,y)

    def __init__(self):
        self.start = time.time()
        self.start_p = time.perf_counter()

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        end = time.time()
        end_p = time.perf_counter()
        runtime = end - self.start
        runtime_p = end_p - self.start_p
        msg = 'The function took {time} seconds to complete'
        print(msg.format(time=runtime))
        msg_p = 'The function took {time} perf seconds to complete'
        print(msg_p.format(time=runtime_p))
