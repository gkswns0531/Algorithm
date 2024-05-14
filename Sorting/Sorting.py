import utils


def bubble_sort(L:list)->None:
    '''
    1. compare two numbers
    2. align bigger to right
    3. outer loop: fix biggest number
    4. shift biggest to right
    '''
    n = len(L)
    for i in range(n-1):
        for j in range(n-i-1):
            if L[j] >= L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return 

def selection_sort(L:list)->None:
    '''
    1. find smallest value in unsorted array
    2. align most left in unsorted array 
    '''
    n = len(L)
    for i in range(n):
        smallest = i
        for j in range(i,n):
            if L[j] <= L[smallest]:
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
            if L[j] <= L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
            else:
                break
    return 



def merge_sort(L:list)->None:
    '''
    1. L -> divide into two sublist
    2. repeat len(sublist) == 1
    3. merge two sublist
    4. use recursion
    '''
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
        if sub_list1[i] <= sub_list2[j]:
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




def quick_sort(L:list)->None:
    '''
    1. select partition (= pivot)
        1) semi sorting ( small comp < pivot < big comp)
    2. L -> divide into two sublist 
    3. use recursion
    '''
    n = len(L)
    quick_sort_help(L,0,n-1)
    return

def quick_sort_help(L:list, start:int, end:int)->None:
    if start >= end:
        return
    else:
        pivot_idx = partition(L,start,end)

        quick_sort_help(L, start, pivot_idx-1)
        quick_sort_help(L, pivot_idx+1, end)
        
def partition(L:list, start:int, end:int)->int:
    pivot = L[end]
    k = start-1 # checking idx: point out comp which is bigger than pivot => k+1 idx > pivot, k idx < pivot

    for i in range(start,end):
        if L[i] <= pivot:
            k += 1
            L[k], L[i] = L[i], L[k]
    k += 1
    L[k], L[end] = L[end], L[k]

    return k

    


if __name__ == "__main__":

    bubble_time = utils.time_complexity(bubble_sort)
    print(f"Selection Sort: {bubble_time}")
    
    selection_time = utils.time_complexity(selection_sort)
    print(f"Selection Sort: {selection_time}")

    insertion_time = utils.time_complexity(insertion_sort)
    print(f"Insertion Sort: {insertion_time}")

    merge_time = utils.time_complexity(merge_sort)
    print(f"Merge Sort: {merge_time}")

    quick_time = utils.time_complexity(quick_sort)
    print(f"Quick Sort: {quick_time}")