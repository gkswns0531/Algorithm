import time

def while_linear_search(L:list, value:int)->int:
    i=0
    n = len(L)
    while (L[i] != value) and (i < n):
        if L[i] != value:
            i += 1

    if i == n:
        i = -1
    
    return i

def while_linear_search_sentinel(L:list, value:int)->int:
    L.append(value)
    i = 0
    n = len(L)
    while L[i] != value:
        i += 1

    if i == n:
        i = -1
    
    L.pop()

    return i

def for_linear_search(L:list, value:int)->int:
    n = len(L)

    for i in range(n):
        if L[i] == value:
            return i
    if i == n-1:
        return -1
    
def for_linear_search_inefficient(L:list, value:int)->int:
    for i in range(len(L)):
        if L[i] == value:
            return i
    if i == len(L)-1:
        return -1

def time_complexity(func, L:list, value:int)->float:
    start_time = time.perf_counter()
    ans = func(L,value)
    end_time = time.perf_counter()

    time_ms = (end_time - start_time) * 1000

    return time_ms



if __name__ == '__main__':
    L = [1 for i in range(1000*10000)]
    L.append(10)
    
    while_linear_search_time = time_complexity(while_linear_search, L, 10)
    sentinel_linear_search_time = time_complexity(while_linear_search_sentinel, L, 10)
    for_linear_search_time = time_complexity(for_linear_search, L, 10)
    for_linear_search_ineff_time = time_complexity(for_linear_search_inefficient, L, 10)

    print(f"While Linear Search: {while_linear_search_time}")
    print(f"Sentinel Linear Search: {sentinel_linear_search_time}")
    print(f"For Linear Search: {for_linear_search_time}")
    print(f"For Linear Search Inefficient: {for_linear_search_ineff_time}")
