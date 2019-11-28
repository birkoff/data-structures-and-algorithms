'''
There are many different versions of quickSort that pick pivot in different ways.

- Always pick first element as pivot.
- Always pick last element as pivot (implemented below)
- Pick a random element as pivot.
- Pick median as pivot.
'''

def find_pivot(a, strategy='middle'):
    if strategy and 'middle' == strategy:
        middle = int(len(a)/2) - 1
        return  middle
        # handle when value is too small or too big if a[middle] <

    if strategy and 'biggest' == strategy:
        biggest = None
        for i in range(len(a)):
            if biggest is None or a[i] > a[biggest]:
                biggest = i
        return biggest


def partition(a, left, right):
    i_left = left # index of the smaller element

    if right >= len(a):
        return

    pivot = a[right] # Always pick last element as pivot

    for i_current in range(left, right):
        current = a[i_current]
        if current <= pivot:
            i_left = i_left + 1
            a[i_left], a[i_current] = a[i_current], a[i_left]

        if (i_left + 1) < len(a):
            a[i_left+1], a[right] = a[right], a[i_left+1]

    return i_left + 1


def quicksort(a, left, right):
    if left < right and right < len(a):
        pi = partition(a, left, right)

        # Separately sort elements before
        # partition and after partition
        if pi is None:
            return

        quicksort(a, left, pi + 1)
        quicksort(a, pi + 1, right)

    #
    # pivot = find_pivot(a)
    # left = 0
    # right = len(a)
    #
    #
    # for i_left in range(len(a)):
    #     if a[i_left] > a[pivot]:
    #
    # return biggest


def find_min_swaps(a):
    arr = a
    n = len(arr)
    quicksort(arr, 0, n-1)
    print("Sorted array is:")
    for i in range(n-1):
        print("%d" % arr[i])


a = [4, 3, 1, 2, 6, 9, 8, 7, 5]
print(find_min_swaps(a))