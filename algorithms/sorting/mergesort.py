def merge_sort(arr):
    print("Current value of array is: {}".format(arr))

    if len(arr) <= 1:
        print("Array len is: {}, skipping".format(len(arr)))
        return

    mid = len(arr)//2  # Finding the mid of the array
    arr_left = arr[:mid]
    arr_right = arr[mid:]

    merge_sort(arr_left)  # sort arr_left side
    merge_sort(arr_right)  # sort right side

    merge_arrays(arr, arr_left, arr_right)


def merge_arrays(arr, arr_left, arr_right):
    print("merge_arrays:  {} + {} => {} ".format(arr_left, arr_right, arr))
    i_left = i_right = k = 0
    while i_left < len(arr_left) and i_right < len(arr_right):
        if arr_left[i_left] < arr_right[i_right]:
            arr[k] = arr_left[i_left]
            i_left += 1
        else:
            arr[k] = arr_right[i_right]
            i_right += 1
        k += 1
    # Checking both sides if any element was left
    # first on left side
    while i_left < len(arr_left):
        arr[k] = arr_left[i_left]
        i_left += 1
        k += 1
    # then with right side
    while i_right < len(arr_right):
        arr[k] = arr_right[i_right]
        i_right += 1
        k += 1

    print("merged_arrays:  {} + {} => {} ".format(arr_left, arr_right, arr))


def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

    print()


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    print_list(arr)
    merge_sort(arr)
    print("Sorted array is: ", end="\n")
    merge_sort(arr)
    print("end")
    print_list(arr)
