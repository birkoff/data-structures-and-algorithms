def buble_sort(arr):
    response = {'sorted': [], 'swaps': 0}

    total = len(arr)-1
    for i in range(total):
        for j in range(total):
            print(j)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                response['swaps'] += 1

    response['sorted'] = arr
    return response


if __name__ == '__main__':
    # arr = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
    # arr = [4, 3, 1, 2, 6, 9, 8, 7, 5]
    # arr = [4, 3, 1, 2]
    arr = [3,2,1]
    response = buble_sort(arr)
    print(response.get('sorted'))
    print("Array is sorted in {} swaps.".format(response.get('swaps')))
    print("First Element: {}".format(response.get('sorted')[0]))
    print("Last Element: {}".format(response.get('sorted')[-1]))