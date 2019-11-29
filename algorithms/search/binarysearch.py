def binary_search(arr,item):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        print("Array mid: {}".format(mid))

        if arr[mid] == item:
            return True

        if item < arr[mid]:
            right = mid - 1 # if item is less than middle move right to the middle - 1
        else:
            left = mid + 1  # if item is more than middle move left to the middle + 1

    return False


if __name__ == '__main__':
    print(binary_search([1,2,3,5,8], 6))
    print(binary_search([1,2,3,5,8], 5))
