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

if __name__ == '__main__':
    L = [1 for i in range(1000*10000)]
    L.append(10)

    while_start = time.perf_counter()
    ans_1 = while_linear_search(L,10)
    while_end = time.perf_counter()
    
    while_linear_search_time = (while_end - while_start) * 1000

    sentinel_start = time.perf_counter()
    ans_2 = while_linear_search_sentinel(L,10)
    sentinel_end = time.perf_counter()
    
    sentinel_linear_search_time = (sentinel_end - sentinel_start) * 1000

    for_start = time.perf_counter()
    ans_3 = for_linear_search(L,10)
    for_end = time.perf_counter()
    
    for_linear_search_time = (for_end - for_start) * 1000

    for_ineff_start = time.perf_counter()
    ans_3 = for_linear_search_inefficient(L,10)
    for_ineff_end = time.perf_counter()
    
    for_linear_search_ineff_time = (for_ineff_end - for_ineff_start) * 1000

    print(f"While Linear Search: {while_linear_search_time}")
    print(f"Sentinel Linear Search: {sentinel_linear_search_time}")
    print(f"For Linear Search: {for_linear_search_time}")
    print(f"For Linear Search Inefficient: {for_linear_search_ineff_time}")
