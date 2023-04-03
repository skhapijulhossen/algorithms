from typing import List, Tuple


def get_two_sum_k(arr: List[int], k: int) -> Tuple:
    """
    ### Time: O(n)    Space: O(2*n)
    """
    if len(arr) < 2 or k < 0:
        return -1

    start, end = 0, len(arr)
    summ = arr[start]
    mapSpace = {}

    while start < end:
        required = k - arr[start]
        found = mapSpace.get(required, None)
        if found:
            return start, found
        mapSpace[arr[start]] = start
        start += 1
    return -1, -1
        


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
        found = get_two_sum_k(arr, k)
        print(f'array={arr} & k={k}:{found}')
