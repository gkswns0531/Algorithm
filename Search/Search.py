import utils

def while_linear_search(L:list, value:int)->int:
    i=0
    n = len(L)
    while (i < n) and (L[i] != value):
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
    
def binary_search(L:list, value:int)->int:
    n = len(L)
    start_idx, end_idx = 0, n-1

    while start_idx < end_idx:
        mid_idx = (end_idx + start_idx)//2
        if L[mid_idx] < value:
            start_idx = mid_idx+1
        else :
            end_idx = mid_idx-1
        
    if start_idx < n and L[start_idx] == value:
        return start_idx
    else:
        return -1


if __name__ == '__main__':
    L = [1 for i in range(1000*10000)]
    L.append(10)
    value = 10
    
    while_linear_search_time = utils.time_complexity(while_linear_search, L, value)
    sentinel_linear_search_time = utils.time_complexity(while_linear_search_sentinel, L, value)
    for_linear_search_time = utils.time_complexity(for_linear_search, L, value)
    for_linear_search_ineff_time = utils.time_complexity(for_linear_search_inefficient, L, value)
    binary_search_time = utils.time_complexity(binary_search, L, value)

    print(f"While Linear Search: {while_linear_search_time[1]}, Ans: {while_linear_search_time[0]}")
    print(f"Sentinel Linear Search: {sentinel_linear_search_time[1]}, Ans: {sentinel_linear_search_time[0]}")
    print(f"For Linear Search: {for_linear_search_time[1]}, Ans: {for_linear_search_time[0]}")
    print(f"For Linear Search Inefficient: {for_linear_search_ineff_time[1]}, Ans: {for_linear_search_ineff_time[0]}")
    print(f"Binary Search: {binary_search_time[1]}, Ans: {binary_search_time[0]}")