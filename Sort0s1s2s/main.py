
# Brute - QuickSort

# Better : Time - O(N*Count(1)), Space - O(1)
def betterSort(data: list[int]) -> list:
    # zero_count, one_count, two_count = 0, 0, 0
    length = len(data)
    left, right = 0, length - 1
    for idx in range(0, length):
        if not (data[idx] ^ 0):
            data[left] = 0
            left += 1
        if not (data[idx] ^ 2):
            data[right] = 2
            right -= 1
    for idx in range(left, right+1):
        data[idx] = 1

    return data


# Optimal - Dutch National Flag Solution
def optimalSort(data: list[int]) -> list:
    length = len(data)
    left, mid,  right = 0, length//2, length - 1

    while mid < right:
        if not (data[mid] ^ 0):
            data[left] = 0
            left += 1
            mid += 1
        if not (data[mid] ^ 1):
            mid += 1
        if not (data[mid] ^ 2):
            data[right] = 2
            right -= 1
            mid += 1    
    return data


if __name__ == '__main__':
    # array = (1,1,2,3,1,4,2,1)
    # out = 4
    # array = (1,1,2,3,1,4,2,1)     k=4
    # out = 3
    # array = (4, 2, 3, 2, 1, 2)    k=5
    # out = 3
    # array = (4, 2, 3, 2, 1, 2)    k=8
    # out = 3


    arrays = [
        [0, 1, 0, 0, 1, 1, 2, 1, 0], [1, 0, 2, 1, 1, 2, 2, 0, 0, 0]
    ]

    # Test
    for arr in arrays:
        print(f'array={arr}')
        sortedData = optimalSort(arr)
        print(f'Sorted:{sortedData}')
