#include <stdio.h>
#include <conio.h>

int divide(int array[], int left, int right)
{
    int pivot = array[left];
    int l = left, r = right;
    while (l < r)
    {
        while (array[l] >= pivot)
        {
            ++l;
        }
        while (array[r] <= pivot)
        {
            --r;
        }
        if (l < r)
        {
            array[l] = array[l] + array[r];
            array[r] = array[l] - array[r];
            array[l] = array[l] - array[r];
        }
        array[left] = array[left] + array[r];
        array[r] = array[left] - array[r];
        array[left] = array[left] - array[r];
        return r;
    }
}

void QuickSort(int array[], int left, int right)
{
    if (left < right)
    {
        int p = divide(array, left, right);
        QuickSort(array, left, p);
        QuickSort(array, p + 1, right);
    }
}

int main()
{
    int i = 0, len;
    printf("\nEnter Length Of Data: ");
    scanf("%d", &len);
    int array[len];
    while (i < len && scanf("%d", &array[i]) == 1)
    {
        i++;
    };
    printf("\nAfter InsertionSort(): ");
    QuickSort(array, 0, 5);
    i = 0;
    while (i < 5)
    {
        printf("%d ", array[i]);
        i++;
    }
    return 0;
}