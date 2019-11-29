def quick_sort(arr, left, right, swaps, pivot_type):
    print("quick_sort: {} {} {}".format(arr, left, right))

    if left >= right:
        print("left >= right, skipping")
        return

    p = partition(arr, left, right, swaps, pivot_type)
    quick_sort(arr, left, p - 1, swaps, pivot_type)
    quick_sort(arr, p + 1, right, swaps, pivot_type)


def partition(arr, left, right, swaps, pivot_type):
    print("partition:  {} = {} {} ".format(arr, left, right))

    pivot = arr[(left + right) // 2]

    if pivot_type == 'left':
        pivot = arr[left]  # pivot is the lower value so we want values to be larger than the pivot
    elif pivot_type == 'right':
        pivot = arr[right]

    low = left + 1
    high = right

    while True:
        #  If the current high value is larger than the pivot everything is OK- we can walk left
        while low <= high and arr[high] >= pivot:
            print("Curren hight: {}".format(arr[high]))
            high -= 1

        #  If the current low value is lower than the pivot everything is OK- we can walk right
        current = arr[low]
        while low <= high and arr[low] <= pivot:
            print("Current low: {}".format(arr[low]))
            low += 1

        # if low is higher than high exit the loop
        if low > high:
            print("low is higher than high exit the loop")
            break

        print("TRY 1 arr[low], arr[high] = {}: {}, {}: {}".format(high, arr[high], low, arr[low]))
        if arr[high] != arr[low]:
            # We found a value for both high and low that is out of order "swap them"
            arr[low], arr[high] = arr[high], arr[low]
            print("SWAP 1 arr[low], arr[high] = {}: {}, {}: {}".format(high, arr[high], low, arr[low]))
            swaps['total'] += 1
            print("########## SWAPS {} #############".format(swaps))

    print(arr)
    print("TRY 2 arr[high], arr[left] = {}: {}, {}: {}".format(high, arr[high], left, arr[left]))
    if arr[left] != arr[high]:
        arr[left], arr[high] = arr[high], arr[left]
        print("SWAP 2 arr[high], arr[left] = {}: {}, {}: {}".format(high, arr[high], left, arr[left]))
        swaps['total'] += 1
        print("########## SWAPS {} #############".format(swaps))

    if pivot_type == 'left':
        return high
    elif pivot_type == 'right':
        return low
    else:
        return (low + high)//2


if __name__ == '__main__':
    # arr = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
    # arr = [4, 3, 1, 2, 6, 9, 8, 7, 5]
    # arr = [4, 3, 1, 2]
    arr = [2, 3, 4, 1, 5]
    swaps = {'total': 0}

    lefty = arr[:1][0]
    rigty = arr[-1:][0]
    total = int(len(arr))

    pivot_type='right'

    if rigty >= total:
        pivot_type = 'left'

    if lefty >= total//2:
        pivot_type = 'left'

    quick_sort(arr, 0, len(arr) - 1, swaps, pivot_type)
    #
    # swaps = {'total': 0}
    # quick_sort(arr, 0, len(arr) - 1, swaps, pivot_type='left')
    #
    # swaps = {'total': 0}
    # quick_sort(arr, 0, len(arr) - 1, swaps)

    print("THE ARRAY AT THE END: {}".format(arr))
    print("Swaps: {}".format(swaps['total']))
