import time

def time_complexity(func, L:list, value:int)->list:
    start_time = time.perf_counter()
    ans = func(L,value)
    end_time = time.perf_counter()

    time_ms = (end_time - start_time) * 1000

    return (ans, time_ms)