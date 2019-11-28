#!/bin/python3


def compare_triplets(a, b):
    points_a, points_b = 0, 0
    for i in range(0, 3):
        if a[i] > b[i]:
            points_a = points_a + 1
        elif b[i] > a[i]:
            points_b = points_b + 1

    print((points_a, points_b))


if __name__ == '__main__':
    # a = [5, 6, 7]
    # b = [3, 6, 10]
    a = [17, 28, 30]
    b = [99, 16, 8]
    compare_triplets(a, b)
