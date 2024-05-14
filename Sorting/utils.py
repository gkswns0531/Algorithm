import time
import random

def time_complexity(func)->list:
    L = [i for i in range(1000)]
    random.shuffle(L)
    print("Before Sorting: ",L[:10])

    start_time = time.perf_counter()
    func(L)
    end_time = time.perf_counter()
    
    print("After Sorting: ",L[:10])

    time_ms = (end_time - start_time) * 1000

    return time_ms