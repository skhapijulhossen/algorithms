
# placing pivot to the right place
def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:

        while i < right and arr[i] < pivot:
            i += 1

        while j >= i and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


# for each Sub Problem / partition
def quickSort(arr, left, right):
    if left < right:
        part = partition(arr, left, right)
        quickSort(arr, left, part - 1)
        quickSort(arr, part + 1, right)


arr = [2, 3, 1, 5, 3, -1, 7, 4, 8]
quickSort(arr, 0, 8)
print(arr)
