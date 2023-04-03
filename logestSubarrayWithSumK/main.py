from typing import List


def get_subarray_sum_k(arr: List[int], k: int) -> int:
    """
    ### Time: O(n)    Space: O(1)
    """
    if len(arr) < 2 or k < 0:
        return -1

    maxlen = 0
    p1, p2 = 0, 1
    summ = arr[p1]

    while p2 < len(arr):
        summ += arr[p2]
        # when summ equals and len is max, update maxlen of sub-array
        if (not summ ^ k) and ((p2 - p1 + 1) > maxlen):
            maxlen = p2 - p1 + 1
        # when summ gets greater than target k, shrink and subtract
        elif summ > k:
            summ -= arr[p1]
            p1 += 1
        p2 += 1
    del summ
    return maxlen


if __name__ == '__main__':
    # array = (1,1,2,3,1,4,2,1)     k=7
    # out = 4
    # array = (1,1,2,3,1,4,2,1)     k=4
    # out = 3
    # array = (4, 2, 3, 2, 1, 2)    k=5
    # out = 3
    # array = (4, 2, 3, 2, 1, 2)    k=8
    # out = 3
    arrays = [
        ((1, 1, 2, 3, 1, 4, 2, 1), 7), ((1, 1, 2, 3, 1, 4, 2, 1), 4),
        ((4, 2, 3, 2, 1, 2), 5), ((4, 2, 3, 2, 1, 2), 8)
    ]
    # Test
    for arr, k in arrays:
        lenth = get_subarray_sum_k(arr, k)
        print(f'array={arr} & k={k}:{lenth}')
