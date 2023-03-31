from typing import List


def get_subarray_sum_k(arr: List[int], k: int) -> int:
    if len(arr)<2 or k<0:
        return -1
    
    maxlen = 0
    p1, p2 = 0, 1
    summ = arr[p1]
    
    while p2<len(arr):
        summ += arr[p2]
        if not sum^k and (p2 - p1 + 1) > maxlen:
            maxlen = p2 - p1 + 1
        elif summ>k:
            p1 += 1
        p2 += 1

    return maxlen


if __name__ == '__main__':
    # array = (1,1,2,3,1,4,2,1)     k=7
    # out = 4
    # array = (1,1,2,3,1,4,2,1)     k=4
    # out = 3
    # array = (1,1,2,3,2,1, 2)    k=5
    # out = 4
    arrays = [((1,1,2,3,1,4,2,1), 7), ((1,1,2,3,1,4,2,1), 4), ((1,1,2,3,2,1, 2), 5)]
    for arr, k in arrays:
        lenth = get_subarray_sum_k(arr, k)