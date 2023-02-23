import timeit
import matplotlib.pyplot as plt
import numpy as np


# implementing the quicksort algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# implementing the merge sort algorithm
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergesort(arr, l, r):
    if l < r:

        m = l + (r - l) // 2


        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        merge(arr, l, m, r)


# implementing the heap sort algorithm
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)


    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


# implementing the insertion sort algorithm
def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# implementing the cocktail sort algorithm
def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):

        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False

        # loop from left to right same as
        # the bubble sort
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # if nothing moved, then array is sorted.
        if (swapped == False):
            break

        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False

        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end - 1

        # from right to left, doing the
        # same comparison as in the previous stage
        for i in range(end - 1, start - 1, -1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # increase the starting point, because the last stage would have moved the next smallest number to its
        # rightful spot.
        start = start + 1


sorts = [
    {
        "name": "Quick Sort",
        "sort": lambda arr: quicksort(arr)
    },
    {
        "name": "Merge Sort",
        "sort": lambda arr: mergesort(arr, 0, len(arr) - 1)
    },
    {
        "name": "Heap Sort",
        "sort": lambda arr: heapsort(arr)
    },
    {
        "name": "Insertion Sort",
        "sort": lambda arr: insertionsort(arr)
    },
    {
        "name": "Cocktail Sort",
        "sort": lambda arr: cocktailSort(arr)
    }
]

elements = np.array([i * 1000 for i in range(1, 10)])

plt.xlabel('Number of elements')
plt.ylabel('Time required, s')

for sort in sorts:
    times = list()
    start_all = timeit.default_timer()
    for i in range(1, 10):
        start = timeit.default_timer()
        a = np.random.randint(10000, size=i * 1000)
        sort['sort'](a)
        end = timeit.default_timer()
        times.append(end - start)

        print(sort["name"], "sorted", i * 1000, "elements in", end - start, "seconds")
    end_all = timeit.default_timer()
    print(sort["name"], "sorted all elements in", end_all - start_all, "seconds")

    plt.plot(elements, times, label=sort["name"])

plt.grid()
plt.legend()
plt.show()
