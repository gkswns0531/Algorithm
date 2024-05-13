import time

def time_complexity(func, L:list)->list:
    start_time = time.perf_counter()
    func(L)
    end_time = time.perf_counter()

    time_ms = (end_time - start_time) * 1000

    return time_ms