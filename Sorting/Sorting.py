
def selection_sort(L:list)->None:
    '''
    1. find smallest value
    2. swap 
    '''
    n = len(L)
    for i in range(n):
        smallest = i
        for j in range(i,n):
            if L[j] < L[smallest]:
                smallest = j
        L[i], L[smallest] = L[smallest], L[i]

    return

