import random
import utils

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

def insertion_sort(L:list)->None:
    '''
    1. select single component in unsorted array
    2. compare with sorted array
    '''
    n = len(L)

    for i in range(1,n):
        for j in range(i,0,-1):
            if L[j] < L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
            else:
                break
    return 

def merge_sort(L:list)->None:
    n = len(L)
    merge_sort_help(L, 0, n-1)


def merge_sort_help(L:list, start:int, end:int)->None:
    if start == end:
        return 
    else:
        mid = start + (end - start) // 2
        merge_sort_help(L,start,mid)
        merge_sort_help(L,mid+1,end)

        merge(L,start,mid,end)

def merge(L:list, start:int, mid:int, end:int)->None:
    k = start
    sub_list1 = L[start:mid+1]
    sub_list2 = L[mid+1:end+1]
    sub1_n = len(sub_list1)
    sub2_n = len(sub_list2)
    i=j=0

    while i < sub1_n and j < sub2_n:
        if sub_list1[i] < sub_list2[j]:
            L[k] = sub_list1[i]
            i += 1
        else:
            L[k] = sub_list2[j]
            j += 1
        k += 1

    if i < sub1_n:
        L[k:end+1] = sub_list1[i:]
    elif j < sub2_n:
        L[k:end+1] = sub_list2[j:]


if __name__ == "__main__":
    
    L = [i for i in range(10000)]
    random.shuffle(L)

    print(L[:10])
    selection_time = utils.time_complexity(selection_sort,L)
    print(L[:10])
    print(selection_time)

    L = [i for i in range(10000)]
    random.shuffle(L)

    print(L[:10])
    insertion_time = utils.time_complexity(insertion_sort,L)
    print(L[:10])
    print(insertion_time)

    # L = [i for i in range(10000)]
    # random.shuffle(L)

    # print(L[:10])
    # merge_time = utils.time_complexity(merge_sort,L)
    # print(L[:10])
    # print(merge_time)