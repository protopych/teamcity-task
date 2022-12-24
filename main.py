import random
import time

''SIZE = 10000


def random_int_array():
    arr = []
    for i in range(0, SIZE):
        arr.append(random.randint(-100, 100))
    return arr


def bubble_sort(arr):
    swapped = True
    n = SIZE
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                temp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = temp
                swapped = True
        n -= 1
    return arr


def qsort(arr, low=0, high=(SIZE - 1)):
    if low < high:
        mid = arr[(low + high) // 2]
        i = low
        j = high
        while i <= j:
            while arr[i] < mid:
                i += 1
            while arr[j] > mid:
                j -= 1
            if i <= j:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i += 1
                j -= 1
        if low < j:
            qsort(arr, low, j)
        if high > i:
            qsort(arr, i, high)


def merge_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])
    n = m = k = 0
    working = [0] * (len(left) + len(right))
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            working[k] = left[n]
            n += 1
        else:
            working[k] = right[m]
            m += 1
        k += 1
    while n < len(left):
        working[k] = left[n]
        n += 1
        k += 1
    while m < len(right):
        working[k] = right[m]
        m += 1
        k += 1
    for i in range(len(arr)):
        arr[i] = working[i]
    return arr


if __name__ == "__main__":
    to_sort_arr = random_int_array()
    bs = to_sort_arr[:]
    qs = to_sort_arr[:]
    ts = to_sort_arr[:]
    ms = to_sort_arr[:]
    start = time.time()
    bubble_sort(bs)
    end = time.time()
    print("Bubble sort: ", round((end - start), 3))
    print(bs == sorted(to_sort_arr))
    start = time.time()
    ts = sorted(ts)
    end = time.time()
    print("Timsort(built-in): ", round((end - start), 3))
    print(ts == sorted(to_sort_arr))
    start = time.time()
    qsort(qs)
    end = time.time()
    print("Quick sort: ", round((end - start), 3))
    print(qs == sorted(to_sort_arr))
    start = time.time()
    merge_sort(ms)
    end = time.time()
    print("Merge sort: ", round((end - start), 3))
    print(ms == sorted(to_sort_arr))
